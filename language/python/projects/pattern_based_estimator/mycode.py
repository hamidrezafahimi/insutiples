import numpy as np
f = np.array([0.0, 2.89, 6.24, 10.94, 35.99, 38.89, 39.07, 39.25, 44.41, 44.49, 42.87, 36.36,
              35.46, 25.96, 9.86, 9.86, 9.77])
g = np.array([5.59, 10.92, 14.74, 19.07, 33.19, 34.40, 35.96, 44.62, 49.18, 33.49, 29.28,
              15.46, 14.16, 7.51, -0.53, -4.39, -6.17])
# initialize predictions for g in based on 3 steps before - None in first 3 steps
g_preds_3_step_forward_lin = [None, None, None]
for i in range(3, len(g)):
    if i == 3:
        g_preds_3_step_forward_lin.append(g[0])
    else:
        linear_pred = g[i-3] + (g[i-3] - g[i-4]) * 3
        g_preds_3_step_forward_lin.append(linear_pred)
sum = 0
for i in range(3, len(g)):
    sum += (g[i]-g_preds_3_step_forward_lin[i]) ** 2
rmse_2 = np.sqrt(sum)
print('rmse is: ', rmse_2)
