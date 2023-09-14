from setuptools import setup

package_name = 'webots_ros2_camera'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/single_camera_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/double_camera_launch.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/single_camera.wbt']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/double_camera.wbt']))
data_files.append(('share/' + package_name + '/resource', ['resource/camera_robot.urdf']))
data_files.append(('share/' + package_name, ['package.xml']))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user.name@mail.com',
    description='Package description',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_robot_with_camera_driver = my_package.my_robot_with_camera_driver:main',
        ],
    },
)
