


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
