import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math as m

def rotate_point(point, phi, theta, psi):
	""" Rotates a given point based on euler angles
	It is equivalent to rotating the old C.S. in which the point lies and get coordinates of the
	point in the new C.S.
	The order of rotation is: 
		rotate by phi (around x) -> rotate by theta (around y) -> rotate by psi (around z)
	Thus, the order of matrix multiplication becomes: Rz(psi) * Ry(theta) * Rx(phi)
	"""
	assert(point.shape == (3,1) or point.shape == (1,3))
	if (point.shape == (1,3)): point = point.T
	if (point.shape == (3,)): 
		point = np.array([[point[0]], [point[1]], [point[2]]])
	def Rx(alpha):
		return np.matrix([[ 1, 0           , 0           ],
						[ 0, m.cos(alpha),-m.sin(alpha)],
						[ 0, m.sin(alpha), m.cos(alpha)]])
	def Ry(alpha):
		return np.matrix([[ m.cos(alpha), 0, m.sin(alpha)],
						[ 0           , 1, 0           ],
						[-m.sin(alpha), 0, m.cos(alpha)]])
	def Rz(alpha):
		return np.matrix([[ m.cos(alpha), -m.sin(alpha), 0 ],
						[ m.sin(alpha), m.cos(alpha) , 0 ],
						[ 0           , 0            , 1 ]])
	R = Rz(psi) * Ry(theta) * Rx(phi)
	return np.array(R * point)

def transform_point(point, phi, theta, psi, T):
	""" Performs a rotation as well as moving the C.S. origin to a given point T
	"""
	assert(T.shape == (3,1) or T.shape == (1,3) or T.shape == (3,))
	if (T.shape == (1,3)): T = T.T
	if (T.shape == (3,)): 
		T = np.array([[T[0]], [T[1]], [T[2]]])
	return np.array(rotate_point(point, phi, theta, psi) + T)


if __name__ == '__main__':
  phi = np.pi/4
  theta = np.pi/2
  psi = 0
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.view_init(elev=45, azim=30)
  pA = np.array([[0],[0],[1]])
  
  # Test rotate_point
  # pB = rotate_point(pA, phi, theta, psi)
  # print(type(pB))
  # ax.plot3D([0, pB[0,0]], [0, pB[1,0]], [0, pB[2,0]], color = 'red')
  # ax.plot3D([0, pA[0,0]], [0, pA[1,0]], [0, pA[2,0]], color = 'green')
  
  # Test transform_point
  t = np.array([[0.5],[0],[0]])
  pB = transform_point(pA, phi, theta, psi, t)
  ax.plot3D([t[0,0], pB[0,0]], [t[1,0], pB[1,0]], [t[2,0], pB[2,0]], color = 'red')
  ax.plot3D([0, pA[0,0]], [0, pA[1,0]], [0, pA[2,0]], color = 'green')
  ax.scatter(t[0], t[1], t[2])
  
  ax.scatter(0, 0, 0)
  ax.set_xlabel("x")
  ax.set_ylabel("y")
  ax.set_zlabel("z")

  plt.show()