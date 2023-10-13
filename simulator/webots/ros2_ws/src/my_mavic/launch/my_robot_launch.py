#!/usr/bin/env python

import os
import pathlib
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.substitutions.path_join_substitution import PathJoinSubstitution
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher


def generate_launch_description():
    package_dir = get_package_share_directory('my_mavic')
    world = LaunchConfiguration('world')
    robot_description = pathlib.Path(os.path.join(package_dir, 'resource', 'my_mavic_webots.urdf')).read_text()

    webots = WebotsLauncher(
        world=PathJoinSubstitution([package_dir, 'worlds', world])
    )

    my_mavic_driver = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        parameters=[
            {'robot_description': robot_description},
        ]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value='my_mavic_world.wbt',
            description='Choose one of the world files from `/my_mavic/worlds` directory'
        ),
        webots,
        my_mavic_driver
    ])
