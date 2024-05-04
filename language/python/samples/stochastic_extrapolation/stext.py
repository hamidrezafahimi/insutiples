import numpy as np
import matplotlib.pyplot as plt
import copy

def predict_linear_probs_recursive(ts, xs, ys, dt, v_std_dev, beta_std_dev, K, num_steps):
    """
    Predicts probabilistic points for multiple time steps using recursive extrapolation.
    
    Args:
        ts (list): List of time points.
        xs (list): List of x-coordinates.
        ys (list): List of y-coordinates.
        dt (float): Time step.
        v_std_dev (float): Standard deviation of velocity.
        beta_std_dev (float): Standard deviation of beta (angle).
        K (int): Number of probabilistic points.
        num_steps (int): Number of time steps to extrapolate.
    
    Returns:
        np.ndarray: Array of shape (num_steps, K, 2) containing probabilistic points.
    """
    assert(num_steps != 0)
    
    l = len(ts)
    assert(l == len(xs) == len(ys) == 2)

    cur_x, last_x = xs[1], xs[0]
    cur_y, last_y = ys[1], ys[0]
    cur_t = ts[1]
    
    vx = (xs[1] - xs[0]) / (ts[1] - ts[0])
    vy = (ys[1] - ys[0]) / (ts[1] - ts[0])
    v = np.sqrt(vx**2 + vy**2)
    vs = np.random.normal(v, v_std_dev, K)

    betas = np.random.normal(0, beta_std_dev, K)
    
    psi = np.arctan2(cur_y - last_y, cur_x - last_x)
    prob_points = []
    for k in range(K):
        r = vs[k] * dt
        dx = r * np.cos(psi + betas[k])
        x = dx + cur_x
        dy = r * np.sin(psi + betas[k])
        y = dy + cur_y
        t = dt + cur_t
        prob_points.append([t, x, y])

    if (num_steps != 1):
        m = num_steps 
        while m > 1:
            next_prob_points = []
            for p in prob_points:
                a_next_prob_point = predict_linear_probs_recursive\
                    ([cur_t, p[0]], [cur_x, p[1]], [cur_y, p[2]], dt, v_std_dev, beta_std_dev, 1, 1)
                next_prob_points.append([a_next_prob_point[0][0], a_next_prob_point[0][1], a_next_prob_point[0][2]])
            m -= 1
            prob_points = []
            prob_points = copy.deepcopy(next_prob_points)

    if (K == 1):
        return prob_points
    else:
        return np.array(prob_points)

# Example usage
ts = [0.2, 0.3]  # Example time points
xs = [2, 3]  # Example x-coordinates
ys = [2, 3]  # Example y-coordinates
dt = 0.05  # Time step
v_std_dev = 1  # Velocity standard deviation
beta_std_dev = 10 * np.pi / 180  # Beta (angle) standard deviation
K = 100  # Number of probabilistic points

plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
for n in range(1, 10):
    plt.cla()
    prob_points = predict_linear_probs_recursive(ts, xs, ys, dt, v_std_dev, beta_std_dev, K, n)
    # Plot the probabilistic points
    print(prob_points)
    for i in range(K):
        plt.scatter(prob_points[i, 1], prob_points[i, 2], alpha=0.2)
        # plt.plot(prob_points[:, i, 0], prob_points[:, i, 1], alpha=0.2)
    plt.scatter(xs, ys, color='red', label='Measured points')
    plt.legend()
    plt.title(f'Probabilistic 2D Path Extrapolation ({n} steps)')
    plt.pause(10)
