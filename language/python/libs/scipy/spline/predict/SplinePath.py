import matplotlib.pyplot as plt
import scipy as sp
import PoseBuffering as pb
import numpy as np

class SplinePathModeler:

    def __init__(self, buf_len = 5):
        self.poseBuffer = pb.Pose1DBuffer(buf_len)

    def predict(self, old_pose, new_time):

        self.poseBuffer.buffer(old_pose)

        if not self.poseBuffer.isFull:
            return None
        
        plt.plot(self.poseBuffer.getT(), self.poseBuffer.getX())
        
        spline = sp.interpolate.CubicSpline(self.poseBuffer.getT(), 
                                            self.poseBuffer.getX(), 
                                            bc_type='natural')
        
        ret = spline(new_time)
        plt.scatter(new_time, ret)
        plt.grid(True)
        plt.show()

        return ret
