

## Creation of an Empty Package

Package creation in ROS 2 uses ament as its build system and colcon as its build tool. You can create a package using either CMake or Python, which are officially supported, though other build types do exist.

1. Package-creation command:

- For a cpp-based package, enter to the workspace source and then:

```
ros2 pkg create --build-type ament_cmake <package_name>
```

- For a python-based package, enter to the workspace source and then:

```
ros2 pkg create --build-type ament_python <package_name>
```

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

### A Typical Robot Simulation Package

Assuming that you have your basical programs (drivers) for your package, this is a summary of what you should do to set-up a practical ROS2 robot simulation package. I assume that your simulation is based on *webots*. Also, I assume that your package is based on python.

For a code sample of each step, refer to [here]().

1. Create an empty package

2. In a general case, create the `worlds/` and `launch/` directories inside your package.

3. Add the script(s) related to your simulation world into the `worlds/` dir.

4. Put your main codes as ROS2 nodes, inside the `package-name/package-name/` dir.

5. If exists, add your *.urdf* files to the `resource/` dir.

6. Inside the `launch/` dir, add a launch file for your robot simulation.

7. In the root of the package, do the proper editions in `setup.py`.

8. Also in the root, do the proper editions in `package.xml`.

9. Go to the workspace and,

```
source install/setup.bash

colcon build
```

10. If the names and addresses have been set correctly, the build must be successful. After a successful build, run your package launch file:

```
source install/setup.bash

ros2 run <pkg-name> <launch-file>.py
```
