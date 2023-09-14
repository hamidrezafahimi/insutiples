#!/usr/bin/env python

import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import argparse
# from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d
from scipy.ndimage.filters import gaussian_filter1d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# objectPath = args.file

objectPath = 'data_1631716287.csv'
dronePath = 'position_2.csv'


colors = ['b', 'r']

label = 'object path'

xs = []
ys = []
with open(objectPath, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    for k, row in enumerate(data):

        if k == 0:
            continue

        xs.append(float(row[1]))
        ys.append(float(row[2]))

    ax.plot(xs, ys, linewidth='3', label = 'Object Path', color = 'r')

ax.set_xlabel("X (m)")
#

maxXs = -1e6
minXs = 1e6
maxYs = -1e6
minYs = 1e6
maxZs = -1e6
minZs = 1e6



xs_ = []
ys_ = []
zs_ = []
with open(dronePath, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    for k, row in enumerate(data):

        if k == 0:
            continue

        xs_.append(float(row[1]))
        ys_.append(float(row[2]))
        zs_.append(float(row[3]))
        # if k == 19200:
        #     ax.scatter(xs_[k-1], ys_[k-1], zs_[k-1], color=(1,0,0), marker="x")

    print(len(xs_))
    ax.plot3D(np.array(xs_), np.array(ys_), np.array(zs_), linewidth='3', label = 'Robot Path', color = 'blue')

    if maxXs < max(xs_):
        maxXs = max(xs_)
    if maxYs < max(ys_):
        maxYs = max(ys_)
    if maxZs < max(zs_):
        maxZs = max(zs_)
    if minXs > min(xs_):
        minXs = min(xs_)
    if minYs > min(ys_):
        minYs = min(ys_)
    if minZs > min(zs_):
        minZs = min(zs_)

midPoint = [(maxXs+minXs)/2, (maxYs+minYs)/2, (maxZs+minZs)/2]
maxDist = max((maxXs-minXs), (maxYs-minYs), (maxZs-minZs))
# ax.set_xlim(midPoint[0]-(maxDist/2), midPoint[0]+(maxDist/2))
# ax.set_ylim(midPoint[1]-(maxDist/2), midPoint[1]+(maxDist/2))
# ax.set_zlim(midPoint[2]-(maxDist/2), midPoint[2]+(maxDist/2))
ax.set_zlim(0, 6)


ax.set_zlabel("Z (m)")





plt.grid()
# line.set_label('Label via method')
ax.legend()
# ax.plot(29.578, 52.748, 'ro')
# print(objectPath)
# if case == 'y':
#     ax.set_ylabel("Avoidance Horizontal Command (m/s)")
#     plt.savefig(objectPath[:-4]+'_y')
# elif case == 'z':
ax.set_ylabel("Y (m)")
plt.savefig(objectPath[:-4]+'_z')


plt.show()
