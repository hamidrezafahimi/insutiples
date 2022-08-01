

### Create a CPP Node inside packege source

1. Write your code inside the `src/` folder of your package

- For a sample publisher, refer to [this link](https://github.com/hamidrezafahimi/technical_utils/blob/main/ROS/ROS2/dev_ws/src/cpp_pubsub/src/publisher_member_function.cpp)

- For a sample subscriber, refer to [this link](https://github.com/hamidrezafahimi/technical_utils/blob/main/ROS/ROS2/dev_ws/src/cpp_pubsub/src/subscriber_member_function.cpp)



2. Navigate to the package root. Open the `package.xml`. Add the dependecies according to your nodes. Like I did below:

```
<depend>rclcpp</depend>
<depend>std_msgs</depend>
```

3. Now in the package root, open the CMakeLists.txt. Do the following editions:

- Add the dependencies:

```
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
```

- For each node that you want to run, add the executables and name them as you wish; So that they may run with ros2 run:

```
add_executable(talker src/publisher_member_function.cpp)
ament_target_dependencies(talker rclcpp std_msgs)
```

- For each executable, add the targets so that the executable is found:

```
install(TARGETS
  talker
  DESTINATION lib/${PROJECT_NAME})
```

4. Source the ROS2 installation in the current terminal.

5. Navigate to the workspace root. Run:

```
colcon build
```

6. To run your nodes, you'll need to do the following in your workspace root:

```
source install/setup.bash
```

7. In such terminal, run your desired node using:

```
ros2 run <pkg> <node>
```


### Create a Python Node inside packege src

1. Write your code inside the `src/` folder of your package

- For a publisher, refer to [this link](https://github.com/hamidrezafahimi/technical_utils/blob/main/ROS/ROS2/dev_ws/src/py_pubsub/py_pubsub/publisher_member_function.py)

- For a subscriber, refer to [this link](https://github.com/hamidrezafahimi/technical_utils/blob/main/ROS/ROS2/dev_ws/src/py_pubsub/py_pubsub/subscriber_member_function.py)

2. Navigate to the package root. Open the `package.xml`. Add the dependecies according to your nodes. Like I did below:

```
<exec_depend>rclpy</exec_depend>
<exec_depend>std_msgs</exec_depend>
```

3. Open the `setup.py`. Inside it, you'll see a field: `entry_point`

By default, it looks like this:

```
entry_points={
        'console_scripts': [
        ],
    },
```

For each executable node, add aline like the following line within the console_scripts brackets of the entry_points field:

```
'talker = py_pubsub.publisher_member_function:main',
```

So for a simple publisher and subscriber node, the entry_points field will look like:

```
entry_points={
        'console_scripts': [
                'talker = py_pubsub.publisher_member_function:main',
                'listener = py_pubsub.subscriber_member_function:main',
        ],
},
```

4. Source the ROS2 installation in the current terminal.

5. Navigate to the workspace root. Run:

```
colcon build
```

6. To run your nodes, you'll need to do the following in your workspace root:

```
source install/setup.bash
```

7. In such terminal, run your desired node using:

```
ros2 run <pkg> <node>
```

### Create a Package with both CPP and Python Nodes

Refer to a [simple tutorial](https://roboticsbackend.com/ros2-package-for-both-python-and-cpp-nodes/) for that, and put a summary here.