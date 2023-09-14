#!/usr/bin/env python

import rosbag
from nav_msgs.msg import Odometry
import pandas as pd
import csv
import argparse
import cv2 as cv
from pathlib import Path
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()
print(args.file)


startIdx = 0
endIdx = 80000

# initPoint = np.array([29.578, 52.748, 4])
initPoint = np.array([0, 0, 0])

def getFileName(path):
    k = len(path)-1
    end = k
    for char in path:
        if path[k] != '/':
            if path[k] == '.':
                end = k
            k -= 1
        else:
            break
    return path[k+1:end]


bagFile = args.file
bag = rosbag.Bag(bagFile)
bagName = getFileName(bagFile)

# Uncomment this part in a case that you need the images:
# from cv_bridge import CvBridge, CvBridgeError
# bridge = CvBridge()
# imgDir = bagName+"images/"
# img_cnt = 0
# Path(imgDir).mkdir(parents=True, exist_ok=True)


xs = []
ys = []
zs = []
ws = []
ts = []

xs_a = []
ys_a = []
zs_a = []

cnt = 0
startTime = 0
# odom_cnt = 0


# for topic, msg, t in bag.read_messages(topics=['/gazebo/model_states']):

#    if topic == '/gazebo/model_states':
#        # print("odom: ", odom_cnt)
#        print('---------------------------------------------')
#        print(msg.pose[9])
#        # print(msg.pose[2].position.x)
#        xs.append(msg.pose[9].position.x)
#        ys.append(msg.pose[9].position.y)
#        zs.append(msg.pose[9].position.z)
       # odom_cnt += 1
# for topic, msg, t in bag.read_messages(topics=['/tello/odom', '/tello/camera/image_raw']):
#     cnt += 1
#     if topic == '/tello/odom' and cnt >= startIdx and cnt <= endIdx:
#        xs.append(np.float32(msg.pose.pose.position.x))
#        ys.append(np.float32(-msg.pose.pose.position.y))
#        zs.append(np.float32(msg.pose.pose.position.z))
#        if startTime == 0:
#            startTime = msg.header.stamp.to_sec()
#        print(msg.header.stamp.to_sec()-startTime)
#        ts.append(msg.header.stamp.to_sec()-startTime)


   # if topic == '/tello/camera/image_raw':
   #     image = bridge.imgmsg_to_cv2(msg, "bgr8")
   #     filename = imgDir+str(img_cnt)+".jpg"
   #     cv.imwrite(filename, image)
   #     img_cnt += 1

for topic, msg, t in bag.read_messages(topics=['/tello/imu', '/tello/cmd_vel']):
    cnt += 1
    # if topic == '/tello/imu' and cnt >= startIdx and cnt <= endIdx:
    #    xs.append(np.float32(msg.orientation.x))
    #    ys.append(np.float32(msg.orientation.y))
    #    zs.append(np.float32(msg.orientation.z))
    #    ws.append(np.float32(msg.orientation.w))
    #    if startTime == 0:
    #        startTime = msg.header.stamp.to_sec()
    #    print(msg.header.stamp.to_sec()-startTime)
    #    ts.append(msg.header.stamp.to_sec()-startTime)

    if topic == '/tello/cmd_vel' and cnt >= startIdx and cnt <= endIdx:
        xs.append(np.float32(msg.linear.x))
        ys.append(np.float32(msg.linear.y))
        zs.append(np.float32(msg.linear.z))
        xs_a.append(np.float32(msg.angular.x))
        ys_a.append(np.float32(msg.angular.y))
        zs_a.append(np.float32(msg.angular.z))


# theta = 90.0*(np.pi/180)
# xs = np.array(xs)*np.cos(theta) + np.array(ys)*np.sin(theta)
# ys = np.array(ys)*np.cos(theta) - np.array(xs)*np.sin(theta)

zeroDist = initPoint - np.array([xs[0], ys[0], zs[0]])
# print(initPoint)
# print(np.array([xs[0], ys[0], zs[0]]))
# print(zeroDist)


# print(ys[200])
# Xs = np.array(xs) + zeroDist[0]
# Xs = -np.array(ys) + zeroDist[0]
# # Ys = np.array(ys) + zeroDist[1]
# Ys = np.array(xs) + zeroDist[1]
# Zs = np.array(zs) + zeroDist[2]

Xs = np.array(ys)
Ys = np.array(xs)
Zs = np.array(zs)
Xs_a = np.array(ys_a)
Ys_a = np.array(xs_a)
Zs_a = np.array(zs_a)
# Ws = np.array(ws)

# xName = 'bagfile_'+bagName+'_x'
# yName = 'bagfile_'+bagName+'_y'
# zName = 'bagfile_'+bagName+'_z'
# wName = 'bagfile_'+bagName+'_w'
xName = 'x_lin'
yName = 'y_lin'
zName = 'z_lin'
# wName = 'w'
xName_a = 'x_ang'
yName_a = 'y_ang'
zName_a = 'z_ang'

# dict = {xName: xs[:-3100], yName: ys[:-3100], zName: zs[:-3100]}
# dict = {xName: Xs, yName: Ys, zName: Zs, wName: Ws, 'time': ts}
dict = {xName: Xs, yName: Ys, zName: Zs, xName_a: Xs_a, yName_a:Ys_a, zName_a:Zs_a}

df = pd.DataFrame(dict)

fileName = 'position_'+bagName+'.csv'

df.to_csv(fileName)
