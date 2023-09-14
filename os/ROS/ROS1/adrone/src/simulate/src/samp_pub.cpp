#include "ros/ros.h"
#include "std_msgs/String.h"

#include <sstream>

/**
 * This tutorial demonstrates simple sending of messages over the ROS system.
 */
int main(int argc, char **argv)
{
  ros::init(argc, argv, "listener"); //This allows ROS to do name remapping through the command line.
                                     // This is also where we specify the name of our node.
  ros::NodeHandle n; //Create a handle to this process' node. The first NodeHandle created will actually do the initialization
                     //of the node,and the last one destructed will cleanup any resources the node was using.
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000); // This invokes a call to the ROS master node. After
                            //this advertise() call is made, the master node will notify anyone who is trying to subscribe to this
                            //topic name. advertise() returns a Publisher object which allows you to publish messages on that topic
                            //through a call to publish(). The second parameter to advertise() is the size of the message queue.
  ros::Rate loop_rate(10);
  int count = 0;
  while (ros::ok())
  {
    std_msgs::String msg; // This is a message object. You stuff it with data, and then publish it.
    std::stringstream ss;
    ss << "hello world " << count;
    msg.data = ss.str();
    ROS_INFO("%s", msg.data.c_str());
    chatter_pub.publish(msg); // The publish() function is how you send messages. The parameter is the message object. The type of
                              // this object must agree with the type given as a template parameter to the advertise<>() call, as
                              // was done in the constructor above.
    ros::spinOnce();
    loop_rate.sleep();
    ++count;
  }
  return 0;
}
