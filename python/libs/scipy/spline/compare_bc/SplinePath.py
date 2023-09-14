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
            return
        
        t = self.poseBuffer.getT()
        x = self.poseBuffer.getX()
        
        plt.scatter(t, x)

        spline1 = sp.interpolate.CubicSpline(t[0:len(t)-2], x[0:len(x)-2], bc_type='not-a-knot')
        spline2 = sp.interpolate.CubicSpline(t[0:len(t)-2], x[0:len(x)-2], bc_type='clamped')
        spline3 = sp.interpolate.CubicSpline(t[0:len(t)-2], x[0:len(x)-2], bc_type='natural')

        t_points = np.linspace(t[0]-0.033, t[len(t)-1]+0.066, num=100)

        plt.plot(t_points, spline1(t_points), label="sp1")
        plt.plot(t_points, spline2(t_points), label="sp2")
        plt.plot(t_points, spline3(t_points), label="sp3")

        plt.legend()
        plt.grid(True)
        plt.show()