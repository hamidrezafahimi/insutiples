#!/usr/bin/env python

import rospy
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np


class MakeVideo:

    def __init__(self):

        self._key = None
        self._finished = False
        self.bridge = CvBridge()
        self._videoWriter = cv.VideoWriter('/home/hamidreza/project_82/papers/paper_2_BD/bd_ws/src/bagProcess/src/output.avi', cv.VideoWriter_fourcc('M','J','P','G'), 30.0, (960,720))
        self.image_sub = rospy.Subscriber("/tello/camera/image_raw",Image,self.imageCallback)

    def imageCallback(self, data):

        if self._finished:
            return

        image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        self._videoWriter.write(image)

        cv.imshow("subscribed video", image)
        self._key = cv.waitKey(10)

        if self._key == ord('q'):
            self._videoWriter.release()
            cv.destroyAllWindows()
            self._finished = True

rospy.init_node('test_node', anonymous=True)

mv = MakeVideo()

rospy.spin()
