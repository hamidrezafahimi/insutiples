import numpy as np
import matplotlib.pyplot as plt
import copy
import time


def calc_2d_psi(p12d, p22d):
    last_x = p12d[0]
    last_y = p12d[1]
    cur_x = p22d[0]
    cur_y = p22d[1]
    return np.arctan2(cur_y - last_y, cur_x - last_x)


def calc_triangular_psi(p12d, p22d, p32d):
    return calc_2d_psi(p22d, p32d) - calc_2d_psi(p12d, p22d)


def predict_linear_probs_1step(olpt, nwpt, dpsi, v_std_dev, beta_std_dev, K):
    dt = (nwpt[0] - olpt[0])
    vx = (nwpt[1] - olpt[1]) / dt 
    vy = (nwpt[2] - olpt[2]) / dt
    v = np.sqrt(vx**2 + vy**2)
    vs = np.random.normal(v, v_std_dev, K)

    betas = np.random.normal(0, beta_std_dev, K)
    olpt2d = [olpt[1], olpt[2]]
    nwpt2d = [nwpt[1], nwpt[2]]
    #psi_ = calc_2d_psi(olpt2d, nwpt2d)
    #print("olpt: ", olpt)
    #print("nwpt: ", nwpt)
    psi = calc_2d_psi(olpt2d, nwpt2d)
    if dpsi is None:
        psi_ = psi
    else:
        psi_ = psi + dpsi
    #print("psi_: ", psi_)
    prb_points = []
    for k in range(K):
        r = vs[k] * dt
        dx = r * np.cos(psi_ + betas[k])
        x = dx + nwpt[1]
        dy = r * np.sin(psi_ + betas[k])
        y = dy + nwpt[2]
        t = dt + nwpt[0]
        prb_points.append([t, x, y])

    if (K == 1):
        return prb_points
    else:
        return np.array(prb_points)


def predict_linear_probs_recursive(parsed_data, v_std_dev=None, beta_std_dev=None, K=None):
    assert(parsed_data is None)
    assert(not v_std_dev is None)
    assert(not beta_std_dev is None)
    assert(not K is None)
    started = False
    next_prob_points = []
    oldpt, newpt = None, None
    while True:
        if started:
            if parsed_data is None:
                buffer, psi = None, None
            else:
                buffer, psi = parsed_data
            if buffer is None:
                #print ("buf is None")
                ## No pose buffer. Extrapolate the last prob points for one step forward 
                assert(len(next_prob_points != 0)) # An initial buffer is needed to start working:
                nnpp = []
                for k in range(K):
                    nwp = new_points[k, :]
                    npp = next_prob_points[k, :]
                    a_next_prob_point = predict_linear_probs_1step \
                        (nwp, npp, psi, v_std_dev, beta_std_dev, 1)
                    nnpp.append([a_next_prob_point[0][0], a_next_prob_point[0][1], a_next_prob_point[0][2]])
                new_points = []
                new_points = np.array(copy.deepcopy(next_prob_points))
                next_prob_points = []
                next_prob_points = np.array(nnpp)
            else:
                #print ("buf is not None")
                ## A pose buffer is passed. The prob points for one forward step must be returned
                oldpt, newpt1 = buffer
                if oldpt is None:
                    # A buffer as (None, newpt) means a new measurement without a previous one
                    assert(not newpt is None) # Not allowed to pass (None, None) as buffer 
                    # Set the prev measurement on last recorded before this step
                    oldpt = newpt
                    newpt = newpt1
                else:
                    newpt = newpt1
                next_prob_points = predict_linear_probs_1step(oldpt, newpt, psi, v_std_dev, beta_std_dev, K)
                new_points = np.array([newpt for k in range(K)])
            #print(" ------ ")
            #print("(det) psi is: ", psi)
            #print("(det) old point: ", oldpt)
            #print("(det) current point: ", newpt)
            #print("(det) next_prob_points: ", next_prob_points)
        else:
            started = True
        parsed_data = yield  next_prob_points  


# Example usage
ts = [0.0, 0.1, 0.2, 0.3]  # Example time points
xs = [-1, 1, 2, 3]  # Example x-coordinates
ys = [0, 1, 2, 3]  # Example y-coordinates

next_ts = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1]  # Example time points
next_xs = [3, 2, 1, 0, -1, -2, -3, -4, -5]  # Example x-coordinates
next_ys = [3, 3, 3, 3, 4, 5, 4, 3, 2]  # Example y-coordinates

ts_after = [1.7, 1.8, 1.9]
xs_after = [-11, -12, -13]
ys_after = [-4, -5, -6]
n_comeback = 17

all_steps_num = 20

v_std_dev = 0.5  # Velocity standard deviation
beta_std_dev = 4 * np.pi / 180  # Beta (angle) standard deviation
K = 50  # Number of probabilistic points

plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
gen = predict_linear_probs_recursive(None, v_std_dev, beta_std_dev, K)
next(gen)
num_of_pose_buffer = len(xs)
num_of_pred_buffer = len(next_xs)
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
old_point, new_point, next_point = None, None, None
for n in range(1, all_steps_num):
    print("log ------------------------------------------------ ")
    plt.cla()
    if (n < num_of_pose_buffer):
        print("predicting for existing pose buffer - index: ", n)
        # This is when the buffer is present and a typical 1-step extrapolation is needed
        old_point = [ts[n-1], xs[n-1], ys[n-1]]
        new_point = [ts[n], xs[n], ys[n]]
        data = ((old_point, new_point), None)
        prob_points = gen.send(data)
    elif (n < (num_of_pose_buffer + num_of_pred_buffer - 1)):
        print("predicting for preferable psi and no pose buffer - indices: ", n, n - num_of_pose_buffer + 1)
        # This is when the buffer is gone and a deterministic extrapolation is to be preferred as: "The mean value for gaussian distribution of stochastic extrapolated points"
        # calc_2d_psi(next_xs[n - num_of_pose_buffer], next_ys[n - num_of_pose_buffer], next_xs[n - num_of_pose_buffer + 1], next_ys[n - num_of_pose_buffer + 1])
        old_point_2d = [old_point[1], old_point[2]]
        new_point_2d = [next_xs[n - num_of_pose_buffer], next_ys[n - num_of_pose_buffer]]
        next_point_2d = [next_xs[n - num_of_pose_buffer + 1], next_ys[n - num_of_pose_buffer + 1]]
        psi_diff = calc_triangular_psi(old_point_2d, new_point_2d, next_point_2d)
        data = (None, psi_diff)
        prob_points = gen.send(data)
        old_point = [0, new_point_2d[0], new_point_2d[1]] 
    elif (n < n_comeback):
        print("predicting linearly with no pose buffer - index: ", n)
        # This is when no deterministic preference is provided, thus extrapolating linearly around last measurements
        prob_points = next(gen)
    elif (n == n_comeback):
        print("predicting for a new measurement - index: ", n)
        new_point = [ts_after[0], xs_after[0], ys_after[0]]
        data = ((None, new_point), None)
        prob_points = gen.send(data)
    else:
        print("predicting for new measurements - index: ", n)
        old_point = [ts_after[n-n_comeback-1], xs_after[n-n_comeback-1], ys_after[n-n_comeback-1]]
        new_point = [ts_after[n-n_comeback], xs_after[n-n_comeback], ys_after[n-n_comeback]]
        data = ((old_point, new_point), None)
        prob_points = gen.send(data)


    # Plot the probabilistic points
    for i in range(K):
        plt.scatter(prob_points[i, 1], prob_points[i, 2], alpha=0.2)
        # plt.plot(prob_points[:, i, 0], prob_points[:, i, 1], alpha=0.2)
    plt.scatter(xs, ys, color='red', label='Measured points')
    plt.plot(xs, ys, color='red')
    plt.scatter(next_xs, next_ys, color='blue', label='Pred points')
    plt.plot(next_xs, next_ys, color='blue')
    plt.legend()
    plt.title(f'Probabilistic 2D Path Extrapolation ({n} steps)')
    plt.pause(2)
