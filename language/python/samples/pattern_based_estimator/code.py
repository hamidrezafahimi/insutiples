
from cProfile import label
import numpy as np
import pandas as pd
import statsmodels.api as sm

import matplotlib.pyplot as plt

# g = np.loadtxt('/home/hamid/w/REPOS/pyTrackers/results/park_mavic_1_target_poses.txt', delimiter=',')[:, 2]
# f = np.loadtxt('/home/hamid/w/REPOS/pyTrackers/results/park_mavic_1_cam_poses.txt', delimiter=',')[:, 2]

f = np.array([0.0, 2.89, 6.24, 10.94, 35.99, 38.89, 39.07, 39.25, 44.41, 44.49, 42.87, 36.36,
              35.46, 25.96, 9.86, 9.86, 9.77])
g = np.array([5.59, 10.92, 14.74, 19.07, 33.19, 34.40, 35.96, 44.62, 49.18, 33.49,
29.28,
15.46,
14.16,
7.51,
-0.53,
-4.39,
-6.17])

# Generate some sample data for f and g
x = np.linspace(0, 1, len(f))
# f = np.sin(2*np.pi*x)
# g = f + np.random.normal(0, 0.1, size=100)

# Fit a linear model to the data
X = sm.add_constant(f)
model = sm.OLS(g, X).fit()
beta_0, beta_1 = model.params

# Make a prediction for g at a new value of f
new_f = 0.2
linear_pred = beta_0 + beta_1 * new_f

print(len(f))
preds = []
# Adjust linear predictions based on known values of f
for i in range(len(f)):
    linear_pred = beta_0 + beta_1 * f[i]
    preds.append(linear_pred)

# for l in [2, 34, 64, 200, 310, 360, 470, 590, 659, 737, 820]:
#     plt.scatter(x[l], f[l])

# for l in [2, 14, 64, 180, 230, 360, 500, 600, 659, 767, 820]:
#     plt.scatter(x[l], g[l])

# for l in [2, 14, 34, 64, 180, 200, 230, 310, 360, 470, 500, 590, 600, 659, 737, 767, 820]:
#     print(g[l])


plt.plot(x, f, label='f')
plt.plot(x, g, label='g')
plt.plot(x, preds, label='preds')
plt.grid(True)
plt.legend()
plt.show()
