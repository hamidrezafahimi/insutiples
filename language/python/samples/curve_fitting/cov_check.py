import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import copy

def func(x, a, b, c):
    return a * np.exp(0.1 * b * x) + c

def func_sine(x, a, b):
    return b*np.sin(a*x)

def func_linear(x, a, b):
    return a * x + b

def func_linear_sine(x, a, b):
    linear = a * x + b
    sine = np.sin(x)
    return linear + sine

def func_poly2(x, a, b, c):
    return a * (x**2) + b * x + c

def func_poly3(x, a, b, c, d):
    return a*(x**3) + b*(x**2) + c*x + d

def get_fitted_curve(func, x, y):
    popt, pcov = curve_fit(func, x, y)
    return func(x, *popt), np.trace(pcov)

def concat_cols(x, y):
    return np.hstack([x.reshape(x.shape[0], 1), y.reshape(y.shape[0], 1)])

def get_fitted_path(f, t, x, y):
    popt_x, pcov_x = curve_fit(f, t, x)
    popt_y, pcov_y = curve_fit(f, t, y)
    tr_x = np.trace(pcov_x)/pcov_x.shape[0] 
    tr_y = np.trace(pcov_y)/pcov_y.shape[0] 
    tr = (tr_x + tr_y)/2
    #print(pcov_x)
    #print(pcov_y)
    #print('---')
    #tr = tr_x + tr_y
    fitted_x = f(t, *popt_x)
    fitted_y = f(t, *popt_y)
    return concat_cols(fitted_x, fitted_y), tr

def optimal_fit(fs, t, x, y):
    best_tr = 1e7
    best_path = None
    K = None
    for k, f in enumerate(fs):
        path, tr = get_fitted_path(f, t, x, y) 
        if tr < best_tr:
            best_tr = tr
            best_path = copy.deepcopy(path)
            K = k
    print(K)
    return best_path



funcs = [func_linear, func_poly2, func_poly3, func_sine]
for k in range(1, 15):
    plt.cla()
    tdata = np.linspace(0, k, 20)
    x = func(tdata, 1.5, 2.3, 0.8)
    #x = func_linear(tdata, 1, 0)
    y = func_sine(tdata, 1, 1)
    rng = np.random.default_rng()
    y_noise = 0.02 * rng.normal(size=tdata.size)
    ydata = y + y_noise
    xdata = x + y_noise
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    
    plt.plot(xdata, ydata, 'b-', label='data')
    path = optimal_fit(funcs, tdata, xdata, ydata) 
    plt.plot(path[:,0], path[:,1], 'r--')
    plt.pause(1)
#plt.plot(tdata, ydata, 'b-', label='y')
#plt.plot(tdata, xdata, 'b-', label='x')

#x_fitter_lin = get_fitted_curve(func_linear, tdata, xdata)
#y_fitter_lin = get_fitted_curve(func_linear, tdata, ydata)
#x_fitter_poly2 = get_fitted_curve(func_poly2, tdata, xdata)
#y_fitter_poly2 = get_fitted_curve(func_poly2, tdata, ydata)
#x_fitter_poly3 = get_fitted_curve(func_poly3, tdata, xdata)
#y_fitter_poly3 = get_fitted_curve(func_poly3, tdata, ydata)


#path_lin, tr_lin = get_fitted_path(func_linear, tdata, xdata, ydata) 
#path_poly2, tr_poly2 = get_fitted_path(func_poly2, tdata, xdata, ydata) 
#path_poly3, tr_poly3 = get_fitted_path(func_poly3, tdata, xdata, ydata) 
#
#plt.plot(path_lin[:,0], path_lin[:,1], 'r--', label='linear fitted - tr: {:2f}'.format(tr_lin))
#plt.plot(path_poly2[:,0], path_poly2[:,1], 'g--', label='poly2 fitted - tr: {:2f}'.format(tr_poly2))
#plt.plot(path_poly3[:,0], path_poly3[:,1], 'y--', label='poly3 fitted - tr: {:2f}'.format(tr_poly3))
#
#plt.xlabel('x')
#plt.ylabel('y')
#plt.legend()
#plt.show()
