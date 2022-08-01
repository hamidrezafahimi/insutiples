

# Creating a ROS2 Workspace

0. To create a ROS2 workspace, you need to have the followings installed:

- ROS2

- colcon build tools


1. Create the workpace folder and a 'src' inside it.

2. Add you packages into the 'src/' directory.

2. in the root of your workspace, 

```
colcon build
```

# Sourcing a ROS2 Workspace

Sourcing the local_setup of the overlay will only add the packages available in the overlay to your environment. setup sources the overlay as well as the underlay it was created in, allowing you to utilize both workspaces.

So you got too ways:

```
# 1.
source /opt/ros/foxy/setup.bash

# 2. Navigate to the workspace root

# 3. Sourcing the  of your workspace
. install/local_setup.bash 
```

And the other equvalent to that:

```
# In the workspace root
source install/setup.bash 
```
