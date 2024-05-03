import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

f = np.array([0.0, 2.89, 6.24, 10.94, 35.99, 38.89, 39.07, 39.25, 44.41, 44.49, 42.87, 36.36,
              35.46, 25.96, 9.86, 9.86, 9.77])
g = np.array([5.59, 10.92, 14.74, 19.07, 33.19, 34.40, 35.96, 44.62, 49.18, 33.49, 29.28,
              15.46, 14.16, 7.51, -0.53, -4.39, -6.17])

xx = range(len(g))

# Initialize predictions for g based on 3 steps before - None in first 3 steps
g_preds_3_step_forward = [None, None, None]

# Train a linear regression model using f and lagged values of g as inputs
X = np.vstack([f[:-3], g[:-3], g[1:-2], g[2:-1]]).T
y = g[3:]
model = LinearRegression().fit(X, y)

# Use the trained model to make predictions for g at each step
for i in range(3, len(g)):
    if i == 3:
        g_preds_3_step_forward.append(g[0])
    else:
        # Predict g using the current value of f and lagged values of g
        X_pred = np.array([f[i], g[i-3], g[i-4], g[i-5]]).reshape(1, -1)
        linear_pred = model.predict(X_pred)
        g_preds_3_step_forward.append(linear_pred)

# Filter out the None values from g_preds_3_step_forward
# g_preds = np.array([x for x in g_preds_3_step_forward if x is not None])
g_preds = []
for x in g_preds_3_step_forward:
    if x is not None:
        if type(x) == np.ndarray:
            g_preds.append(x[0])
        else:
            g_preds.append(x)

# Calculate the RMSE between the predicted and actual values of g
rmse = np.sqrt(np.mean((g[3:len(g_preds)+3] - g_preds) ** 2))
print('RMSE is:', rmse)


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

plt.plot(xx, f, label='f')
plt.plot(xx, g, label='g')
plt.plot(xx[3:], g_preds, label='g_preds_3_step_forward')
plt.plot(xx, g_preds_3_step_forward_lin, label='g_preds_3_step_forward_lin')
plt.grid(True)
plt.legend()
plt.show()