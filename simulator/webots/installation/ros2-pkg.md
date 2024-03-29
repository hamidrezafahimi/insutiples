

## Installation on ROS2

This is enough to install webots with ROS2.

Remember that you should have the ros2 installed.

```
sudo apt-get install ros-<ros-distro>-webots-ros2
```

During installation, if you do not have the webots installed, it'll be installed in `$HOME/.ros/` directory. Otherwise, when launcing first time, it asks you and installs the simulator.

## Check the installation 

Run:

```
source /opt/ros/<ros-distro>/setup.bash

ros2 launch webots_ros2_mavic robot_launch.py 
```

In a new terminal:

```
source /opt/ros/<ros-distro>/setup.bash

ros2 topic list
```

And you'll be able to see the ros2 topics enabled by the robot.



### Access from terminal
To access the webots from your terminal:

```
cd ~

gedit .bashrc
```

Now add the following to the end of your `.bashrc`:

```
export PATH="$PATH:$HOME/.ros/webotsR2022a/webots"
```

Then in a new terminal:

```
webots
```

Should start up your empty webots.
