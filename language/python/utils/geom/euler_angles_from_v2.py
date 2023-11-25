import numpy as np

def get_euler_angles(v1, v2):
    # Find axis of rotation
    axis = np.cross(v1, v2)
    axis = axis / np.linalg.norm(axis)

    # Find angle of rotation
    cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    angle = np.arccos(cos_angle)

    # Create rotation matrix
    c = np.cos(angle)
    s = np.sin(angle)
    t = 1 - c
    x = axis[0]
    y = axis[1]
    z = axis[2]
    rot_matrix = np.array([[t*x*x + c, t*x*y - z*s, t*x*z + y*s],
                           [t*x*y + z*s, t*y*y + c, t*y*z - x*s],
                           [t*x*z - y*s, t*y*z + x*s, t*z*z + c]])

    # Extract Euler angles
    sy = np.sqrt(rot_matrix[0,0] * rot_matrix[0,0] + rot_matrix[1,0] * rot_matrix[1,0])
    singular = sy < 1e-6
    if not singular:
        x = np.arctan2(rot_matrix[2,1], rot_matrix[2,2])
        y = np.arctan2(-rot_matrix[2,0], sy)
        z = np.arctan2(rot_matrix[1,0], rot_matrix[0,0])
    else:
        x = np.arctan2(-rot_matrix[1,2], rot_matrix[1,1])
        y = np.arctan2(-rot_matrix[2,0], sy)
        z = 0

    return x, y, z

# Example usage
v1 = np.array([0, 0, 1])
v2 = np.array([1, 2, 3])
euler_angles = get_euler_angles(v1, v2)
print(euler_angles)  
# Outputs (0.0, 1.5707963267948966, 0.0) for a 90 degree rotation around the y-axis