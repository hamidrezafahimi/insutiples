
import rospy
import rosbag

# import sys
# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import argparse
import os
import glob
import pandas as pd
import csv
import time


parser = argparse.ArgumentParser()
parser.add_argument("mode")
parser.add_argument("file")
args = parser.parse_args()


class ProcessImageBags:

    def __init__(self):

        self._key = None
        self._finished = False
        self.bridge = CvBridge()
        self._bagTopic = '/tello/camera/image_raw'
        self.image_pub = rospy.Publisher('/test_frames', Image, queue_size=10)
        self._infoFileName = "/info.csv"


    def read(self, address):

        mainNum = 0
        totalNum = 0
        with open(address + self._infoFileName, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

            # for i, d in enumerate(data[0]):
            #     if d == 'finalFrame':
            #         mainNum = int(data[1][i])
            #     elif d == 'specialTime':
            #         mainTime = float(data[1][i])

            I = None
            for i, d in enumerate(data[0]):
                if d == 'time':
                    I = i
                    break
            mainTime = data[len(data)-1][I]
            # totalNum = len()
            # for k, row in enumerate(data):
            #     prms.append(row[2])

        totalNum = len(data)
        num = len(glob.glob(address + "/*.jpg"))
        kk = 0
        k = 0
        while k <= mainNum:
            k += 1
            if not os.path.exists(address + "/img_" + str(k) + ".jpg"):
                kk += 1

        newRate = num/float(mainTime)
        print('newRate', newRate)

        flag = True
        t1 = time.time()
        k = 1
        print('kk',kk)
        while k <= totalNum:

            file = address + "/img_" + str(k) + ".jpg"
            if not os.path.exists(file):
                k += 1
                continue

            image = cv.imread(file)
            print(k)
            cv.imshow("published video", image)
            key = cv.waitKey(1)
            self.image_pub.publish(CvBridge().cv2_to_imgmsg(image, "bgr8"))
            rospy.Rate(newRate).sleep()

            if key == ord('q'):
                break
            elif key == ord('w'):
                flag = True
            elif key == ord('e'):
                flag = False
            if flag:
                print('infinite loop')
                continue
            k += 1

        T = time.time() - t1
        print('elapsed time: ', T)


    def show(self, address):
        mainNum = 0
        with open(address + self._infoFileName, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            ### OLD:
            # mainTime = float(data[1][5])
            # for i, d in enumerate(data[0]):
            #     if d == 'specialTime':
            #         mainTime = float(data[1][i])
            #         break
            ### NEW:
            I = None
            for i, d in enumerate(data[0]):
                if d == 'time':
                    I = i
                    break
            mainTime = data[len(data)-1][I]

        mainNum = len(glob.glob(address + "/*.jpg"))
        print(mainTime)
        rate = mainNum/float(mainTime)
        k = 1
        t1 = None
        kk = 0
        file1 = address + "/fe_" + str(kk) + ".jpg"
        img = cv.imread(file1)
        flag = False

        ### for: meeting, math, aero
        flag1 = False
        ### for: chem,
        # flag1 = True
        while k <= 5100:
            flag2 = False
            file = address + "/file_" + str(k) + ".jpg"
            if not os.path.exists(file):
                k += 1
                continue
            image = cv.imread(file)
            dim = (692, 520)
            image = cv.resize(image, dim, interpolation = cv.INTER_AREA)

            if flag1 or (not (t1 is None) and (t2 - t1) > 4):
                kk += 1
                print(kk)
                file1 = address + "/opt/fe_" + str(kk) + ".jpg"
                if os.path.exists(file1):
                    img = cv.imread(file1)
                    flag = True
                    flag2 = True
                    flag1 = False

            if flag:
                dim = (1800, 400)
                img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
                cv.imshow("DAE Parameter Optimization", img)
                t2 = time.time()
                if flag2:
                    t1 = time.time()
                cv.moveWindow("DAE Parameter Optimization",100,600)

            cv.imshow("Robot Camera Image", image)
            cv.moveWindow("Robot Camera Image",100,0)

            key = cv.waitKey(int(1000/rate))

            if key == ord('q'):
                break
            elif key == ord('w'):
                flag1 = True

            k += 1


    def write(self, bagFile):

        address = self.extractFileAddress(bagFile)
        name = self.getFileName(bagFile)
        bag = rosbag.Bag(bagFile)

        newAddress = address + name
        print(address)
        print(name)
        if not os.path.exists(newAddress):
            path = os.path.join(address, name)
            os.mkdir(path)

        it = 0
        its = []
        perms = []
        ts = []
        start = 0
        end = 1e10
        ff = -2
        flag = True
        for topic, msg, t in bag.read_messages(topics=[self._bagTopic]):
            if topic == self._bagTopic:
                if it == 0:
                    start = msg.header.stamp.to_sec()

                it += 1

                image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
                cv.imshow("subscribed video", image)

                filename1 = newAddress + "/img_%d.jpg"%it
                its.append(it)
                if flag:
                    perms.append(1)
                else:
                    perms.append(0)
                end = msg.header.stamp.to_sec()
                relativeTime = end-start
                ts.append(relativeTime)
                txt = str(relativeTime)
                print(txt)
                image = cv.putText(image, txt, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 
                                1, (255, 0, 0), 2, cv.LINE_AA)

                cv.imwrite(filename1, image)
                self._key = cv.waitKey(1)
                if self._key == ord('q'):
                    break
                elif self._key == ord('w'):
                    specialEnd = msg.header.stamp.to_sec()
                    flag = False
                    ff = it

        dict = {'imgs': its, 'permissions': perms, 'time':ts}
        df = pd.DataFrame(dict)
        fileName = newAddress + self._infoFileName
        df.to_csv(fileName)
        print('write done')


    def getFileName(self, path):

        flag = True
        k = len(path)
        end = k-1

        for char in path:
            k -= 1

            if path[k] == '.' and flag:
                flag = False
                end = k

            if path[k] == '/':
                break

        return path[k+1:end]


    def extractFileAddress(self, path):

        flag = True
        k = len(path)
        end = k-1

        for char in path:
            k -= 1

            if path[k] == '/':
                end = k+1
                break
        return path[0:end]


rospy.init_node('test_node', anonymous=True)

mv = ProcessImageBags()

if args.mode == "read":
    mv.read(args.file)

elif args.mode == "write":
    mv.write(args.file)

elif args.mode == "show":
    mv.show(args.file)


rospy.spin()
