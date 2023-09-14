#include "ros/ros.h"
#include "std_msgs/String.h"

 void chatterCallback(const std_msgs::String::ConstPtr& msg)  //This is the callback function that will get
 {                                                            // called when a new message has arrived on the chatter topic
   ROS_INFO("I heard: [%s]", msg->data.c_str());
 }

 int main(int argc, char **argv)
 {

   ros::init(argc, argv, "listener"); //This allows ROS to do name remapping through the command line.
                                      //This is also where we specify the name of our node.

   ros::NodeHandle n;   //Create a handle to this process' node. The first NodeHandle created will actually do the initialization
                        //of the node,and the last one destructed will cleanup any resources the node was using.

   ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback); //Subscribe to the __ topic with the master. ROS will
                                                                        // call the chatterCallback() function whenever a new
                                                                        // message arrives. The 2nd argument is the queue size.
                                                                        // if the queue reaches _ messages, we will start.
                                                                        // throwing away old messages as new ones arrive.
   ros::spin(); //enters a loop, calling message callbacks as fast as possible. will exit once ros::ok() returns false, which
                // means ros::shutdown() has been called, either by the default Ctrl-C handler, or it being called manually.
   return 0;
  }
