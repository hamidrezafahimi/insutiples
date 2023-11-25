import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from euler_rotation import transform_point

def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


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

    line = [1, 2, 3]
    draw_pyramid(ax, 1, 60, 60, t, -0.5880026035475675, 
                 0.27054976297857286, -0.0823726211170212, 'red')
    # # draw_pyramid(ax, height, hfov, vfov, t, yaw=0, pitch=0, roll=0)
    # draw_pyramid(ax, height, hfov, vfov, t, yaw=np.pi/4, pitch=0, roll=0, facecolors='yellow')

    ax.plot3D([t[0,0], line[0]], [t[1,0], line[1]], [t[2,0], line[2]])
    ax.scatter([t[0,0]], [t[1,0]], [t[2,0]])

    set_axes_equal(ax)

    plt.show()