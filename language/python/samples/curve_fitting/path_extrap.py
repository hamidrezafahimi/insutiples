from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import copy

def func_linear(x, a, b):
    return a * x + b

def func_poly2(x, a, b, c):
    return a * (x**2) + b * x + c

def func_poly3(x, a, b, c, d):
    return a*(x**3) + b*(x**2) + c*x + d


def concat_cols(x, y):
    return np.hstack([x.reshape(x.shape[0], 1), y.reshape(y.shape[0], 1)])


def get_fitted_path(f, t, x):
    popt_x, pcov_x = curve_fit(f, t, x)
    tr_x = np.trace(pcov_x)/pcov_x.shape[0] 
    fitted_x = f(t, *popt_x)
    return fitted_x, tr_x


def optimal_fit(t, x):
    best_tr = 1e9
    best_path = None
    fs = [func_linear, func_poly2, func_poly3]
    for f in fs:
        path, tr = get_fitted_path(f, t, x) 
        if tr < best_tr:
            best_tr = tr
            best_path = copy.deepcopy(path)
    return best_path


def linear_curve_fit(ts, _pos_buff, new_times=None, t=None):
    t0 = ts[0]
    ts_ = np.array([t-t0 for t in ts])
    fitted_path = optimal_fit(ts_, _pos_buff)
    print("inputs: ------------ ")
    print(ts)
    print(_pos_buff)
    print(t)
    return linear(ts, fitted_path, new_times, t), fitted_path

def linear(ts, _pos_buff, new_times=None, t=None):#,_interp_factor=1):
    ## calculate velocities for each consecutive pair of buffered target positions (used to 
    ## estimate a current velocity for the target)
    v = (_pos_buff[-1] - _pos_buff[-2]) / (ts[-1] - ts[-2])
    if not new_times is None:
        outs = []
        for n in new_times:
            dt = n - ts[-1]
            outs.append(_pos_buff[-1] + v*dt)
            # outs.append(_pos_buff[-1] + _interp_factor*v*dt)
        print("outputs: -------------- ")
        print(v)
        print(dt)
        print(outs)
        return outs  
    elif not t is None:
        dt = t - ts[-1]
        out = _pos_buff[-1] + v*dt
        return out
    else:
        raise Exception("One of 'new_times' or 't' must be set")


if __name__ == '__main__':
    ts =np.array([0.,         0.16969991, 0.33939981, 0.50909972, 0.67879963, 0.84849954 , 1.01819944, 1.18789935, 1.35759926, 1.52729917])

    xs = np.array([-15.6964013,  -15.69719765, -15.67215335, -15.08594338, -14.71809189 , -14.69170368, -14.66531548, -14.63892727, -14.61253906, -14.52380518])

    ys =np.array([ 6.31103896,  6.4121457,   6.5001097,   7.30348526,  8.72206871,  8.79927482 ,  8.87648093,  8.95368704,  9.03089315, 10.89814851])

    t = np.array([1.52729917,1.72729921])
    _, xfit = linear_curve_fit(ts, xs, t)
    _, yfit = linear_curve_fit(ts, ys, t)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    
    plt.plot(xs, ys, 'b-', label='data')
    plt.plot(xfit, yfit, 'r-', label='data')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    #
