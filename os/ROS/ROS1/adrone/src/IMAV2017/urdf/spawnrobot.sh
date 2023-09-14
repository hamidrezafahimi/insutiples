#!/bin/bash

rosrun xacro xacro --inorder quadrotor.urdf.xacro id:=$1 > qws.urdf
rosrun gazebo_ros spawn_model -file qws.urdf -urdf -model quadrotor_$1 -x -18 -y 13 -z 3
