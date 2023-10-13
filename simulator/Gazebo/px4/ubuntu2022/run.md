
This is instruction to run only the Gazebo simulation developed by PX4. I was surprised getting aware of the fact that - as I know at least in their Gazebo-classic simulations - their simulated drone has no mounted camera; And people are arguing in the forums about how to add a camera to their models without problem - specially critical for ROS2! Anyway, why would you need a simulation when no camera is mounted on your drone?!

Generally, you must do the following before running, to provide ros2-PX4 communications:

- New terminal:

```
MicroXRCEAgent udp4 -p 8888
```

Then in a new terminal:

```
cd PX4-Autopilot
```

They may also offer you to source the PX4:

```
source Tools/simulation/gazebo-classic/setup_gazebo.bash $(pwd) $(pwd)/build/px4_sitl_default
source ~/.bashrc	# Once saw a suggestion for this in an issue
```

Next, see the followings note for the run commands.


**NOTE:** An important thing that I figured out installing PX4 on ubuntu22, was the fact that,

- When I did the last step (`make px4_sitl`) without Gazebo installed on my host, the modern case of gazebo (previously known as gazebo-ignition) would launch with `x500` drone model. I.e. the following command would work, and not the gazebo-classic cases.
```
make px4_sitl gz_x500
```

- Otherwise, when I installed Gazebo doing [this](), the following command would work, and not the above one:
```
make px4_sitl gazebo-classic
```

The above launchs the defaullt case. More generic Gazebo-classic Run Commands:

```
# From PX4 root - typical command:
Tools/simulation/gazebo-classic/sitl_multiple_run.sh -m <vehicle-model> -n <vehicles-num> -w <world>
#sample:
Tools/simulation/gazebo-classic/sitl_multiple_run.sh -m iris -n 2 -w empty
```

