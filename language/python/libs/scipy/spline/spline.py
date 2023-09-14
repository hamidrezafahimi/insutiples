import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.interpolate

x = np.arange(-3, 4)
y = x**2

plt.scatter(x, y)

# spline1 = sp.interpolate.CubicSpline(x, y, bc_type='not-a-knot')
# spline2 = sp.interpolate.CubicSpline(x, y, bc_type='periodic')
# spline3 = sp.interpolate.CubicSpline(x, y, bc_type='clamped')
spline3 = sp.interpolate.CubicSpline(x, y, bc_type=((2,2), (2,2)))
spline4 = sp.interpolate.CubicSpline(x, y, bc_type='natural')

x_points = np.linspace(x[0]-1, x[len(x)-1]+2, num=100)
# plt.plot(x_points, spline1(x_points), label="sp1")
# plt.plot(x_points, spline2(x_points), label="sp2")
plt.plot(x_points, spline3(x_points), label="sp3")
plt.plot(x_points, spline4(x_points), label="sp4")

plt.legend()
plt.grid(True)
plt.show()