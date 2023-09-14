# Technical Utils

This is the result of my *don't-throw-little-stuff-away* routine! A set of go-to programs archived together. The repo contains two types of programs:

* Starting a new project, I follow some tutorials and make primary samples before entering the main job. I put all of them here.

* Sometimes I find it necessary to create simple programs (e.g. reading or writing some special filetypes, plotting specia shapes, dealing with special libraries, etc.) which are pretty simple while taking time to do them again. So, I can store them all in my little *Technical Utils* box. Maybe they work for other people, Why not.

*NOTE:* To get the most out of what is presented here, remember to check my [instruction set](https://github.com/hamidrezafahimi/instructor_archive) if needed. There, lie all of the steps taken to install, compile, or run the softwares that their modifications are given here.

## Some Important Featurs

Here is a list of the most important modules and utilities provided in this repo:

* Simple codes to extract and plot data out of ROS1 bagfiles: [Link](https://github.com/hamidrezafahimi/technical_utils/tree/main/ROS1/process_bagfiles). ([description](#plotting)) 

* A drone flight simulation, using the *IMAV2017* virtual challenge platform, based on Gazebo-7 and ROS1: [Link](https://github.com/hamidrezafahimi/technical_utils/tree/main/ROS1/adrone) ([description](#adrone))

* A stand-alone drone flight simulation for ROS2 and based on *webots 2022a*: [Link](https://github.com/hamidrezafahimi/technical_utils/tree/main/ROS2/webots_ws/src/my_mavic) ([description](#src/my_mavic))

* Simulation of a stand-alone single camera in webots - May seem easy but I didn't find such thing!:[Link](https://github.com/hamidrezafahimi/technical_utils/tree/main/ROS2/webots_ws/src/webots_ros2_camera) ([description](#src/webots_ros2_camera))

## Tutorials and Samples

* Elementary samples fo gazebo simulation based on ROS1: [Link](https://github.com/hamidrezafahimi/technical_utils/tree/main/ROS1/gi5m) ([description](#gi5m))

* How to simply create a Makefile to compile cpp codes: [Link](https://github.com/hamidrezafahimi/technical_utils/tree/main/cpp/class/makefile) ([description](#CPP))

* How to create a simple `CMakeLists.txt` file in order to compile and run cpp codes: [Link](https://github.com/hamidrezafahimi/technical_utils/tree/main/cpp/simple/cmake) ([description](#CPP))

* How to create a `CMakeLists.txt` file for an object oriented cpp project with standard filesystem: [Link](https://github.com/hamidrezafahimi/technical_utils/tree/main/cpp/simple/cmake) ([description](#CPP))

# Working Tree Explained

All the folders contain non-related programs and are just classified based on their context. The following working tree shows what's going on here.

## plotting

The directory includes some useful programs for drawing plots in python's *matplotlib* platform.

## ROS1

### adrone

Here, I've dumped the junk - and of course the successful results - that I collected during my attempts to simulate a quadrotor in the gazebo. Maybe one day I will arrange it so that it takes the form of a respectable document. I don't have time now!

### gi5m

This is how I simply learned Gazebo: My 2019 homeworks following the instructions given in [this course](https://www.youtube.com/playlist?list=PLK0b4e05LnzbHiGDGTgE_FIWpOCvndtYx).

### process_bagfiles

Contains a bunch of python scripts which handle the extraction and plotting of data saved in ROS1 bagfiles.


## ROS2

Each folder is a ROS2 workspace.

### dev_ws

A Practice of Creating Workspace, Package, Nodes, etc. This is the tutorial is based on what is given in the ROS2 documentaion. 

- [Creating Workspaces](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html)

- [Creating Packages](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html)

- [Creating CPP Publisher and Subscriber](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Cpp-Publisher-And-Subscriber.html)

- [Creating Python Publisher and Subscriber](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)

### samples_ws

In this workspace, the useful ROS2 samples are placed to be a simple tutorial and avoid doing ROS2 simple tasks again. For example, the `src/cmd_vel_pub` is a simple velocity commant publisher which can be modified to control robots based on ROS2 platform.

### webots_ws

This is the workspace of my webots projects. I put the initial sample of my webots works here.

#### src/my_package

This is the performed [ros2 official documentation tutorial](https://docs.ros.org/en/foxy/Tutorials/Advanced/Simulators/Webots.html) for simulating robots with ros2. 

#### src/my_mavic

This guy is so useful. It's a native simulation of Mavic 2 Pro, totally stand-alone and independent of ros2-webots installation directories.

#### src/webots_ros2_camera

If you're to work with webots and ROS2, and you need a camera, here it is. I've made and upoaded it as a ROS2 package with required python driver. 

## webots

The webots worlds that I've created so far.


## CPP

Samples to run cpp codes with different paradigms (gcc, makefile, cmake). Also including simplifications on C++ features, pointers on how to set-up a filesystem for C++ project, and so on. Each of the basic contents shape a sub-directory. Within, different folders contain different compilation paradagms - if exist! - around the same context.