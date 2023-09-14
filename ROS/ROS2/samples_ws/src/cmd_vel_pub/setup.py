from setuptools import setup

package_name = 'cmd_vel_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hamid',
    maintainer_email='hamidrfahimi@gmail.com',
    description='Package description',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = cmd_vel_pub.cmd_vel_pub:main',
        ],
    },
)
