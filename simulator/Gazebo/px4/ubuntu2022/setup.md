

[Source](https://docs.px4.io/main/en/ros/ros2_comm.html)

1. Install PX4:

```
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
bash ./PX4-Autopilot/Tools/setup/ubuntu.sh
cd PX4-Autopilot/
make px4_sitl
```

2. [Install ROS](https://github.com/hamidrezafahimi/insutiples/blob/main/os/ROS/ROS2/instructions/installation/ros-2-foxy-on-ubuntu-2020-extended.md)

3. Setup Micro XRCE-DDS Agent & Client in a terminal:

```
git clone https://github.com/eProsima/Micro-XRCE-DDS-Agent.git
cd Micro-XRCE-DDS-Agent
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig /usr/local/lib/
```

Setup done! Check [how-to-run](https://github.com/hamidrezafahimi/insutiples/blob/main/simulator/Gazebo/px4/ubuntu2022/run.md) to run simulation.


