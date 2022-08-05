

```
cd PX4-Autopilot
make px4_sitl_rtps gazebo

export LANG=C.UTF-8
export LC_ALL=C.UTF-8

DONT_RUN=1 make px4_sitl_default gazebo

sudo apt upgrade libignition-math4

source Tools/setup_gazebo.bash $(pwd) $(pwd)/build/px4_sitl_default
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)/Tools/sitl_gazebo
roslaunch px4 mavros_posix_sitl.launch
```
