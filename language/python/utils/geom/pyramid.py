import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from euler_rotation import transform_point

def draw_pyramid(ax, height, hfov_deg, vfov_deg, pose, yaw, pitch, roll, facecolors='cyan'):
	wx = 2 * height * np.tan((hfov_deg * np.pi / 180) / 2)
	wy = 2 * height * np.tan((vfov_deg * np.pi / 180) / 2)
	cpose = transform_point(np.array([[0], [0], [0]]), yaw, pitch, roll, pose)
	c1 = transform_point(np.array([[-wx], [-wy], [height]]), yaw, pitch, roll, pose)
	c2 = transform_point(np.array([[wx], [-wy], [height]]), yaw, pitch, roll, pose)
	c3 = transform_point(np.array([[wx], [wy], [height]]), yaw, pitch, roll, pose)
	c4 = transform_point(np.array([[-wx], [wy], [height]]), yaw, pitch, roll, pose)
    # vertices of a pyramid
	v = np.array([list(*c1.T), list(*c2.T), list(*c3.T), list(*c4.T), list(*cpose.T)])
	ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
    # generate list of sides' polygons of our pyramid
	verts = [ [v[0],v[1],v[4]], [v[0],v[3],v[4]],
    	[v[2],v[1],v[4]], [v[2],v[3],v[4]], [v[0],v[1],v[2],v[3]]]
    # plot sides
	ax.add_collection3d(Poly3DCollection(verts, 
        facecolors=facecolors, linewidths=1, edgecolors='r', alpha=.25))

if __name__ == '__main__':
    ax = plt.figure().add_subplot(111, projection='3d')
    ax.view_init(elev=45, azim=30)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    t = np.array([[0],[0],[0]])
    height = 1
    hfov = 30
    vfov = 30

    draw_pyramid(ax, height, hfov, vfov, t, yaw=0, pitch=0, roll=0)
    # draw_pyramid(ax, height, hfov, vfov, t, yaw=np.pi/4, pitch=0, roll=0, facecolors='yellow')

    plt.show()