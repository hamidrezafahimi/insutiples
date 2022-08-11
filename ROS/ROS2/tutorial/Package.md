

## Creation of an Empty Package

Package creation in ROS 2 uses ament as its build system and colcon as its build tool. You can create a package using either CMake or Python, which are officially supported, though other build types do exist.

1. Package-creation command:

### CPP Package

For a cpp-based package, enter to the workspace `src/` and then:

```
ros2 pkg create --build-type ament_cmake <package_name>
```

### Python Package

For a python-based package, enter to the workspace `src/` and then:

```
ros2 pkg create --build-type ament_python <package_name>
```

*NOTE:* The `test/` directory which is built automatically inside the package by ros2, can be removed. It's not neccessary.

*NOTE:* Also, you can delete the `__init__.py` file inside the `pkg/pkg/` directory.

*NOTE:* There is an empty file with the name of the package and no extension inside the `resource/` directory. DON'T remove it. It's important.

2. Then build the workspace:

```
# In the root of <ws_dir>

colcon build
```

Or build only the desired package:

```
colcon build --packages-select <package_name>
```


## Setting Up a Package

### A Typical Robot Simulation Package - Python

Assuming that you have your basical programs (drivers) for your package, this is a summary of what you should do to set-up a practical ROS2 robot simulation package. I assume that your simulation is based on *webots*. Also, I assume that your package is based on python.

For a code sample of each step, refer to [here]().

1. Create an empty package

2. In a general case, inside your package:

```
mkdir worlds launch
```

3. Add the script(s) related to your simulation world into the `worlds/` dir.

4. Put your main codes as ROS2 nodes, inside the `package-name/package-name/` dir.

5. If exists, add your *.urdf* files to the `resource/` dir.

6. Inside the `launch/` dir, add a launch file for your robot simulation.

7. In the root of the package, do the proper editions in `setup.py`.

8. Also in the root, do the proper editions in `package.xml`.

9. Go to the workspace and,

```
source /opt/ros/<ROS_DISTRO>/setup.bash

colcon build
```

10. If the names and addresses have been set correctly, the build must be successful. After a successful build, run your package launch file:

```
source install/setup.bash

ros2 run <pkg-name> <launch-file>.py
```

#### What to do when changing the filenames?

The names of the files in a python-based package are declared in `setup.py` and also the launch files. That means if you're going to change the names of your files (e.g. launch file(s), node(s), etc.), then you will:

- Edit the `setup.py` based on new names.

- Edit the launch files within `launch/` directory

- Do a `rm -r build install log` in your workspace and build it again with `colcon build`
