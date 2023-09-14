from scipy.interpolate import interp1d, BSpline
import matplotlib.pyplot as plt
import numpy as np


x = [5,6,7,8,9,10,11]
y = [2,9,6,3,4,20,6]

xx = np.linspace(0, 15, 1000)
 
f = interp1d(x, y, kind='quadratic', fill_value='extrapolate') 
yy = f(xx)

plt.scatter(x, y)
plt.plot(xx, yy, label='quadratic-extrap')
plt.grid(True)
plt.show()