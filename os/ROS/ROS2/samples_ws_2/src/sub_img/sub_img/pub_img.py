#!/usr/bin/env python3
# Revision $Id$


import rclpy
from rclpy.node import Node
# from custom_batch.msg import Batch #### import custom message
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
import numpy as np

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Image, 'Image', 10) #### change here
        timer_period = 0.033  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.im_list = []
        self.cv_image1 = cv2.imread('/home/hamid/w/DATA/bagimgs/img0000.jpg')
        # self.cv_image2 = cv2.imread('2.jpg')
        self.bridge = CvBridge()

    def timer_callback(self):

        #### custom message
        # my_msg = Image()
        # my_msg.data = self.bridge.cv2_to_imgmsg(np.array(self.cv_image1), "bgr8")
        my_msg = self.bridge.cv2_to_imgmsg(self.cv_image1, encoding="passthrough")
        # my_msg.data[0] = self.bridge.cv2_to_imgmsg(np.array(self.cv_image1), "bgr8")
        # my_msg.data[1] = self.bridge.cv2_to_imgmsg(np.array(self.cv_image2), "bgr8")
        #####
        self.publisher_.publish(my_msg) ## custom message
        self.get_logger().info('Publishing an image')

def main(args=None):

    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
     main()