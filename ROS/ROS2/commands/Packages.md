

Enter to the workspace source:

```
cd <ws_dir>/src

ros2 pkg create --build-type ament_cmake <package_name>
```

Then build the workspace:

```
# In the root of <ws_dir>

colcon build
```

Or build only the desired package:

```
colcon build --packages-select <package_name>
```
