

In this directory, I describe how I performed a personalized px4-gazebo-iris simulation under ros2. It is so simple:

1. Look at the companion file `iris.sdf.jinja`. Replace it with the co-name file in your `PX4-Autopilot/Tool/simulation/gazebo-classic/sitl_gazebo-classic/models/iris` directory. I have added a camera to it.

2. There is also a companion world file named `personal.world` in the current directory. Move it into your `PX4-Autopilot/Tool/simulation/gazebo-classic/sitl_gazebo-classic/worlds` directory. Note that this is just a sample. Create your personal desired world and do the same thing to perform simulation in your desired environment.

3. You probably have cutom `sdf` models included in your world script. I also have one. It is in the companion directory `my_model`. Move it into your `PX4-Autopilot/Tool/simulation/gazebo-classic/sitl_gazebo-classic/models` directory. You know that you can add your desired model to your world script adding something like the following to it:
```
<include>
	<uri>model://my_model</uri>
</include>
```

3. To run the simulation, in one terminal:
```
MicroXRCEAgent udp4 -p 8888
```
And in another one:
```
cd PX4-Autopilot

Tools/simulation/gazebo-classic/sitl_multiple_run.sh -n 1 -m iris
```
