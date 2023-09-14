Running Simulation in ROS 2

New Terminal

```
 cd ~/PX4-Autopilot/ \
&&  make px4_sitl_rtps gazebo
```


New Terminal

```
source ~/px4_ros_com_ros2/install/setup.bash \
&& micrortps_agent -t UDP
```

New Terminal

```
source ~/px4_ros_com_ros2/install/setup.bash \
&& ros2 run px4_ros_com offboard_control
```
