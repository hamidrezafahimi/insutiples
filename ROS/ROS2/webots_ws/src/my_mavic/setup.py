from setuptools import setup

package_name = 'my_mavic'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/my_robot_launch.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/my_mavic_world.wbt']))
data_files.append(('share/' + package_name + '/resource', ['resource/my_mavic_webots.urdf']))
data_files.append(('share/' + package_name, ['package.xml']))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hamid',
    maintainer_email='hamidrfahimi@gmail.com',
    description='Package description',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_mavic_driver = my_mavic.my_mavic_driver:main'
        ],
    },
)

