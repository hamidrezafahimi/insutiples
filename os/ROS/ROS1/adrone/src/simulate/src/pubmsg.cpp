#include "ros/ros.h"
#include "std_msgs/String.h"
#include "geometry_msgs/Twist.h"
// #include "std_msgs/Float64.h"
#include "simulate/imtodyn.h"
#include <sstream>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "dyncon"); // This allows ROS to do name remapping through the command
                                     //line. This is also where we specify the name of our node.
  ros::NodeHandle n; // Create a handle to this process' node. The first NodeHandle created will actually do the initialization
                     //of the node,and the last one destructed will cleanup any resources the node was using.
  ros::Publisher pub = n.advertise<simulate::imtodyn>("tttopic", 10);  // This invokes a call to the ROS
                     //master node. After this advertise() call is made, the master node will notify anyone who is trying to
                     //subscribe to this topic name. advertise() returns a Publisher object which allows you to publish messages on
                     //that topic through a call to publish(). The second parameter to advertise() is the size of the message queue.
  ros::Rate loop_rate(10); // Loop at 10Hz

  // geometry_msgs::Twist msg;
  //
  // msg.linear.x = 0.0;
  // msg.linear.y = 0.1;
  // msg.linear.z = 0.0;
  // msg.angular.x = 0;
  // msg.angular.y = 0;
  // msg.angular.z = 0.0;

  simulate::imtodyn msg;

  // msg.header.stamp = ros::Time::now();
  // msg.header.frame_id = "/world";
  msg.x = 1.0;

  int count = 0;
  while (ros::ok())
  {
    pub.publish(msg); // The publish() function is how you send messages. The parameter is the message object. The type of
                              // this object must agree with the type given as a template parameter to the advertise<>() call, as
                              // was done in the constructor above.
    ros::spinOnce();
    loop_rate.sleep();
    ++count;
  }
  return 0;
}
