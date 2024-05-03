import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

def func_sine(x):
    return np.sin(x)

def func_linear(x, a, b):
    return a * x + b

def func_poly2(x, a, b, c):
    return a * (x**2) + b * x + c

def get_fitted_curve(func, x, y):
    popt, pcov = curve_fit(func, x, y)
    return func(x, *popt)

# Define the data to be fit with some noise:

tdata = np.linspace(0, 4, 50)
x = func(tdata, 1.5, 2.3, 0.8)
y = func_sine(tdata)
rng = np.random.default_rng()
y_noise = 0.01 * rng.normal(size=tdata.size)
ydata = y + y_noise
xdata = x + y_noise
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')

fitted_x = get_fitted_curve(func_poly2, tdata, xdata)
fitted_y = get_fitted_curve(func_poly2, tdata, ydata)
fitted_yofx_path = get_fitted_curve(func_poly2, xdata, ydata)
fitted_xofy_path = get_fitted_curve(func_poly2, ydata, xdata)

plt.plot(xdata, ydata, 'b-', label='data')
plt.plot(fitted_x, fitted_y, 'r--', label='time fitted')
plt.plot(xdata, fitted_yofx_path, 'g--', label='fitted_yofx_path')
plt.plot(fitted_xofy_path, ydata, 'y--', label='fitted_xofy_path')


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
