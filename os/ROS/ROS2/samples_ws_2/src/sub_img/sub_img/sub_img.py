import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import time
import collections
import numpy as np
from cv_bridge import CvBridge
import cv2 

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Image,
            '/camera_image_gray',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.t = None
        self.ts = collections.deque(maxlen = 100)
        self.br = CvBridge()

    def listener_callback(self, msg):
        current_frame = self.br.imgmsg_to_cv2(msg)
        # cv2.imshow("camera", current_frame)   
        # cv2.waitKey(1)
        if self.t is None:
            self.t = time.time()
            return
        dif = time.time() - self.t
        self.ts.append(dif)
        print("Image subscription dt: {:2f}".format(np.mean(self.ts)))
        self.t = time.time()

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
   # Destroy the node explicitly
   # (optional - otherwise it will be done automatically
   # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
