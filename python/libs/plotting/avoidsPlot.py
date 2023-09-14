#!/usr/bin/env python

import sys

# ros_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'
# if ros_path in sys.path:
#
#     sys.path.remove(ros_path)
import cv2 as cv
# sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')

import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
from scipy.signal import find_peaks
import csv
from scipy.ndimage.filters import gaussian_filter1d
import glob
import os

plt.rcParams["font.family"] = "Times New Roman"
plt.rc('legend',fontsize=16)
plt.rcParams["legend.loc"] = 'lower left'
# plt.rc('legend', loc = 1)

def getFileName(path):
    flag = True
    k = len(path)-1
    end = k
    for char in path:
        if path[k] != '/':
            if path[k] == '.' and flag:
                flag = False
                end = k
            k -= 1
        else:
            break
    return path[k+1:end]

# imdir = 'home/hamidrea/project_82/paper_2_BD/plots/imgSource/'
imdir = 'imgSource/imgs/'
mapdir = 'imgSource/depthMaps/'
# ext = ['png']    # Add image formats here

files = []
mapFiles = []
files.extend(sorted(glob.glob(imdir + '*.png')))
mapFiles.extend(sorted(glob.glob(mapdir + '*.png')))

print(files)
print(mapFiles)
#
images = [cv.imread(file) for file in files]
maps_ = [cv.imread(file) for file in mapFiles]

# cv.imshow("df", maps[0])
# cv.waitKey()
# plt.rcParams["font.family"] = "Times New Roman"
# print(files)

imgs = []
maps = []
xs = []
for file in files:
    xs.append(np.double(getFileName(file)[7:]))

print(xs)
#
for img in images:
    img = cv.resize(img, (470, 470))
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    imgs.append(img)
#
for img_ in maps_:
    img = cv.resize(img_, (470, 470))
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    maps.append(img)
#

fn = ['data_1631281753yy.csv', 'data_1631281753zz.csv']

colors = ['b', 'r']

labels = ['Lateral', 'Vertical']

fig, ax = plt.subplots()

# fig = plt.figure()
#
# ax = fig.add_subplot(111)

ax.set_ylim(-1.1,5)
ax.set_xlim(2.2,7.54)

for kk, fileName in enumerate(fn):
    ts = []
    ys = []

    with open(fileName, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

        for k, row in enumerate(data):

            if k == 0:
                continue

            ts.append(float(row[3]))
            ys.append(float(row[1]))

        if kk == 0:
            ys = np.array(ys)*12
        else:
            ys = -np.array(ys)*6

        ts = np.array(ts)

        # ysmoothed = ys
        ysmoothed = gaussian_filter1d(ys, sigma=2)
        ysmoothed[0] = 0
        ax.plot(ts[20:-75], ysmoothed[20:-75], linewidth='3', label = labels[kk] , color = colors[kk])
        # print(len(xs))
#
xxs = np.linspace(3.0, 7.0, num=7)
# xxs = np.delete(xxs, 4)
for k, i in enumerate(xxs):
    ax.axvline(x=i, ymin=0.0, ymax=1.0, color='black', linewidth=1, linestyle='--')

    binImg = imgs[k]
    imagebox = OffsetImage(binImg, zoom=0.2)
    ab1 = AnnotationBbox(imagebox, (i, 2.4))
    ax.add_artist(ab1)

    map = maps[k]
    mapbox = OffsetImage(map, zoom=0.2)
    ab2 = AnnotationBbox(mapbox, (i, 4))
    ax.add_artist(ab2)

# plt.xlabel(r'$\tau$ (%)', fontsize=16)
# plt.ylabel(r'$C_{(\tau)}$', fontsize=16)
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(22)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(22)
#

t = ("Detected\n"
     "Obstacles")
plt.text(2.65, 2.4, t, fontsize=18, ha='center', rotation=90, wrap=True)
plt.text(2.65, 4.0, "TTC Map", fontsize=18, ha='center', rotation=90, wrap=True)

plt.draw()

ax.set_xlabel("time (sec)", fontsize=22)

plt.grid()

ax.legend()

ax.set_ylabel("Avoidance Commands (m/s)",  fontsize=22)
plt.savefig(fileName[:-4]+'_z.pdf')

plt.show()
