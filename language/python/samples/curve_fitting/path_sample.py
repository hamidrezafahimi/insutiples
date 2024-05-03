import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(0.1 * b * x) + c

def func_sine(x):
    return np.sin(x)

def func_linear(x, a, b):
    return a * x + b

def func_linear_sine(x, a, b):
    linear = a * x + b
    sine = np.sin(x)
    return linear + sine

def func_poly2(x, a, b, c):
    return a * (x**2) + b * x + c


# Define the data to be fit with some noise:

tdata = np.linspace(0, 7, 50)
x = func(tdata, 1.5, 2.3, 0.8)
y = func_sine(tdata)
rng = np.random.default_rng()
y_noise = 0.01 * rng.normal(size=tdata.size)
ydata = y + y_noise
xdata = x + y_noise
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')

plt.plot(xdata, ydata, 'b-', label='data')
#plt.plot(tdata, ydata, 'b-', label='y')
#plt.plot(tdata, xdata, 'b-', label='x')
for k, x in enumerate(xdata):
    print(x,',', ydata[k])


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
