cmake_minimum_required(VERSION 2.8.3)
project(simulate CXX)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  genmsg
  sensor_msgs
  cv_bridge
  image_transport
  OpenCV REQUIRED
  geometry_msgs
  message_generation
)
   #-Dlibsdl-dev_DIR=/usr/share/doc
#find_package(libsdl1.2-dev REQUIRED)


#link_directories(/usr/share/doc/libsdl1.2-dev)



 add_message_files(
   FILES
   imtodyn.msg
   dyntoim.msg
#   Message2.msg
 )


generate_messages(
  DEPENDENCIES
  std_msgs
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES simulate
  CATKIN_DEPENDS message_runtime
#  DEPENDS system_lib
)


include_directories(
 include
  ${catkin_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIRS}
)


add_executable(impro src/impro.cpp)
add_executable(dyncon src/dyncon.cpp)
add_executable(pubmsg src/pubmsg.cpp)


target_link_libraries( impro ${OpenCV_LIBS} )
target_link_libraries(impro ${catkin_LIBRARIES})
target_link_libraries(dyncon ${catkin_LIBRARIES})
target_link_libraries(pubmsg ${catkin_LIBRARIES})

add_dependencies(impro ${catkin_EXPORTED_TARGETS})
add_dependencies(dyncon ${catkin_EXPORTED_TARGETS})
add_dependencies(pubmsg ${catkin_EXPORTED_TARGETS})
