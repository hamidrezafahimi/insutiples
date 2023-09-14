#!/usr/bin/env python

import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import argparse

plt.rcParams["font.family"] = "Times New Roman"

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()
print(args.file)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


maxXs = -1e6
minXs = 1e6
maxYs = -1e6
minYs = 1e6
maxZs = -1e6
minZs = 1e6

# ax.plot3D([2.75, 3.75, 3.75, 2.75, 2.75], [-5, -5, -5, -5, -5] , [8, 8, 9.5, 9.5, 8], 'r')
ax.plot3D([-5, -5, -5, -5, -5], [2.75, 3.75, 3.75, 2.75, 2.75] , [8, 8, 9.5, 9.5, 8], 'r')

fileName = args.file

if fileName == "all":
    all = [
    'new_921_position_data/position_2021-12-05-18-47-47.csv',
    'new_921_position_data/position_2021-12-05-18-55-39.csv',
    'new_921_position_data/position_2021-12-05-19-00-15.csv',
    'new_921_position_data/position_2021-12-05-19-10-36.csv',
    'new_921_position_data/position_2021-12-05-19-17-06.csv',
    'new_921_position_data/position_2021-12-05-19-20-48.csv',
    'new_921_position_data/position_2021-12-05-19-31-06.csv',
    'new_921_position_data/position_2021-12-05-19-35-09.csv']
    # 'position_2020-11-21-19-23-45.csv',
    # 'position_2020-11-21-19-34-25.csv', #ha
    #  # 'position_2020-11-21-15-35-25.csv', #na
    #  'position_2020-11-21-19-41-55.csv', #na
    # # 'position_2020-11-21-18-32-28.csv' , #na
    # 'position_2020-11-21-19-45-02.csv', #ha ?
    # 'position_2020-11-21-18-56-02.csv' , #ha
    # # 'position_2020-11-21-19-50-38.csv', # na
    # # 'position_2020-11-21-19-13-39.csv' , na
    #  # 'position_2020-11-21-19-57-03.csv' #hA
     # ]

    # NOTE: The Filed Test: 'position_2020-11-21-19-50-38.csv'
else:
    all = [fileName]

colors = ['red','orange','green','blue','brown','black','purple','pink']

kkk = -1
for fileName in all:
    kkk += 1
    print(fileName)
    xs = []
    ys = []
    zs = []
    with open(fileName, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

        for k, row in enumerate(data):

            if fileName == 'new_921_position_data/position_2021-12-05-19-00-15.csv' and k < 2000:
                continue

            if fileName == 'new_921_position_data/position_2021-12-05-18-47-47.csv' and k < 3200:
                continue

            if k == 0:
                continue

            xs.append(float(row[1]))
            ys.append(float(row[2]))
            zs.append(float(row[3]))
            if k == 19200:
                ax.scatter(xs[k-1], ys[k-1], zs[k-1], color=(1,0,0), marker="x")

        print(len(xs))
        ax.plot3D(np.array(xs), np.array(ys), np.array(zs), colors[kkk])
        # ax.plot3D(np.array(ys), np.array(xs), np.array(zs), colors[kkk])

        if maxXs < max(xs):
            maxXs = max(xs)
        if maxYs < max(ys):
            maxYs = max(ys)
        if maxZs < max(zs):
            maxZs = max(zs)
        if minXs > min(xs):
            minXs = min(xs)
        if minYs > min(ys):
            minYs = min(ys)
        if minZs > min(zs):
            minZs = min(zs)


plt.locator_params(axis='x', nbins=6)
plt.locator_params(axis='y', nbins=6)
plt.locator_params(axis='z', nbins=6)
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(14)
for tick in ax.zaxis.get_major_ticks():
    tick.label.set_fontsize(14)
#
# ax.plot3D([-5, -5, -5, -5, -5], [2.75, 3.75, 3.75, 2.75, 2.75] , [8, 8, 9.5, 9.5, 8], 'r')


# axx=ax.get_axes()
# azm=axx.azim
# ele=axx.elev
# dst=axx.dist
ax.view_init(elev=45, azim=135) #Works!

midPoint = [(maxXs+minXs)/2, (maxYs+minYs)/2, (maxZs+minZs)/2]
maxDist = max((maxXs-minXs), (maxYs-minYs), (maxZs-minZs))
ax.set_xlim(midPoint[0]-(maxDist/2), midPoint[0]+(maxDist/2))
ax.set_ylim(midPoint[1]-(maxDist/2), midPoint[1]+(maxDist/2))
# ax.set_zlim(midPoint[2]-(maxDist/2), midPoint[2]+(maxDist/2))
ax.set_zlim(5, 15)

ax.set_xlabel("x (m)", fontsize=16)
ax.set_ylabel("y (m)", fontsize=16)
ax.set_zlabel("z (m)", fontsize=16)

# plt.axis('off')

# plt.savefig(figName)
plt.show()
