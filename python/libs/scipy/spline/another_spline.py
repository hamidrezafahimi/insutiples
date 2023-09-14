import scipy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

def plotNow(plot=None, scatter=None, pause=0.001):
    plt.cla()
    if not plot is None:
        for p in plot:
            plt.plot(p[0], p[1])
    if not scatter is None:
        for s in scatter:
            plt.scatter(s[0], s[1])
    plt.grid(True)
    plt.show()

data = pd.read_csv("/home/hamid/d/BACKUPED/tcs-9-3/data/VIOT/park_mavic_1/new/park_mavic_1_target_poses.txt", header=None)
data = np.array(data)

l = len(data)

buf_len = 10
pred_len = 10

for k in range((buf_len-1), l-6):
    ts = data[k-(buf_len-1):k+1,0]
    vals = data[k-(buf_len-1):k+1,1]
    new_times = data[k:k+(pred_len-1),0]
    pred_true_vals = data[k:k+(pred_len-1),1]

    # vals = savgol_filter(vals, buf_len, 4) # window size 51, polynomial order 3

    # first_derivative_new = (vals[len(vals)-1] - vals[len(vals)-2]) / (ts[len(ts)-1] - ts[len(ts)-2])
    # first_derivative_old = (vals[len(vals)-2] - vals[len(vals)-3]) / (ts[len(ts)-2] - ts[len(ts)-3])
    # second_derivative = (first_derivative_new - first_derivative_old) / (ts[len(ts)-1] - ts[len(ts)-2])
    # spline = sp.interpolate.CubicSpline(ts, vals, bc_type=((2, 0), (1, first_derivative_new)))

    spline = sp.interpolate.CubicSpline(ts, vals, bc_type='natural')

    # spline = sp.interpolate.CubicSpline(ts, vals, bc_type='not-a-knot')
    
    new_vals = []
    for n in new_times:
        new_vals.append(spline(n))
    
    plotNow(plot=[[ts,vals],
                #   [data[:,0], data[:,1]],
                  [new_times,pred_true_vals],
                  [new_times,new_vals]], 
            pause=0.5)
    
    
    
