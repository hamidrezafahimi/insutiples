import rclpy

class CameraDriver:

    def init(self, webots_node, properties):

        self.__robot = webots_node.robot
        rclpy.init(args=None)
        self.__node = rclpy.create_node('camera_driver')

    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0)
