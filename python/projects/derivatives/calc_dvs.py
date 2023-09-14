import numpy as np
import matplotlib.pyplot as plt

def calc_1st_dv(inp, t, idx):
    if idx == 0 or idx >= len(t) or len(inp) != len(t):
        raise Exception("bad input")
    return ((inp[idx]-inp[idx-1])/(t[idx]-t[idx-1]))

def calc_2nd_dv(inp, t, idx):
    if idx == 0 or idx >= len(t) or len(inp) != len(t):
        raise Exception("bad input")
    return ((calc_1st_dv(inp, t, idx)-calc_1st_dv(inp, t, idx))/(t[idx]-t[idx-1]))

def calc_1st_dv_all(inp, t):
    out = []
    for k in range(1, len(inp)):
        out.append((inp[k]-inp[k-1])/(t[k]-t[k-1]))
    return out

def calc_2nd_dv_all(inp, t):
    out = []
    out = []
    for k in range(2, len(inp)):
        out.append((calc_1st_dv(inp, t, k)-calc_1st_dv(inp, t, k-1))/(t[k]-t[k-1]))
    return out
    

x = np.linspace(-3, 4, 1000)
y = x**2

yd = calc_1st_dv_all(y, x)
ydd = calc_2nd_dv_all(y, x)

plt.plot(x, y, label='main')
plt.plot(x[1:], yd, label='1st deriv')
plt.plot(x[2:], ydd, label='2nd deriv')
plt.legend()
plt.grid(True)
plt.show()