 #include <ros/ros.h>
 #include <image_transport/image_transport.h>   //includes everything we need to publish and subscribe to images.
 #include <opencv2/highgui/highgui.hpp>
 #include <cv_bridge/cv_bridge.h>

 void imageCallback(const sensor_msgs::ImageConstPtr& msg)    //will get called when a new image has arrived on the
 {      //"camera/image" topic. Although the image may have been sent in some arbitrary transport-specific message type,
   try  // notice that the callback need only handle the normal sensor_msgs/Image type. All image encoding/decoding is
   {    //handled automagically
     cv::imshow("view", cv_bridge::toCvShare(msg, "bgr8")->image);  //We convert the ROS image message to an OpenCV image
     cv::waitKey(30);                                               //with BGR pixel encoding, then show it in a display window.
   }
   catch (cv_bridge::Exception& e)
   {
     ROS_ERROR("Could not convert from '%s' to 'bgr8'.", msg->encoding.c_str());
   }
 }

 int main(int argc, char **argv)
 {
   ros::init(argc, argv, "image_listener");
   ros::NodeHandle nh;
   cv::namedWindow("view");
   cv::startWindowThread();
   image_transport::ImageTransport it(nh);      //We create an ImageTransport instance, initializing it with our NodeHandle.
                                                // We use methods of ImageTransport to create image publishers and subscribers,
                                                // much as we use methods of NodeHandle to create generic ROS publishers & subscribers.
   image_transport::Subscriber sub = it.subscribe("camera/image", 1, imageCallback); //Subscribe to the "camera/image" base topic. The
                                                                                     //actual ROS topic subscribed to depends on which
                                                                                     //transport is used. In the default case, "raw"
                                                                                     //transport, the topic is in fact "camera/image"
                                                                                     // with type sensor_msgs/Image. ROS will call the
                                                                                     //"imageCallback" function whenever a new image
                                                                                     //arrives. The 2nd argument is the queue size.
   ros::spin();
   cv::destroyWindow("view");
 }
