#include "ros/ros.h"
#include "std_msgs/String.h"
#include "geometry_msgs/Twist.h"
#include "simulate/imtodyn.h"
#include "simulate/dyntoim.h"
#include <sstream>
using namespace std;

float vy, vz;
bool flag = false, enterance = false, lost = false;
int staticIt=0;

void dataCallback(const simulate::imtodyn msg)
{
  flag = true;
  vy = -(0.005*msg.y);
  vz = -(0.005*msg.z);
  enterance = msg.enterance;
  cout<<"dyncon subscribed data\tvy:"<<vy<<"\tvz:\t"<<vz<<endl;
}



int main(int argc, char **argv)
{
  float gain = 1, vey, vez;
  ros::init(argc, argv, "dyncon");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("visual_info", 1, dataCallback);
  ros::Publisher pub = n.advertise<geometry_msgs::Twist>("quadrotor_1/cmd_vel", 10);
  ros::Publisher pubBack = n.advertise<simulate::dyntoim>("dynamic_feedback", 1);
  ros::Rate loop_rate(10); // Loop at 10Hz
  int count = 0, subCount = 0, t = 0 ;
  geometry_msgs::Twist gmsg;
  simulate::dyntoim bmsg;

  vey = gain*vy;
  vez = gain*vz;



  while (ros::ok())
  {
    cout<<"dyncon flag:\t"<<flag<<"\tentrance flag:  "<<enterance<<endl;



    if(flag){
      if(count<10) gmsg.linear.x = 0.2;
      else if(count<30) gmsg.linear.x = 0.3;
      else if(count<40) gmsg.linear.x = 0.4;
      else if(count<50) gmsg.linear.x = 0.5;
      // if (count>100) gmsg.linear.x = 0.68;
      // else if(count>200) gmsg.linear.x = 0.85;
      // else if(count>300) gmsg.linear.x = 1;
      else gmsg.linear.x = 0.6;
      // gmsg.linear.x = 0.5;
      // if(vy>0.75) gmsg.linear.y = vy;
      /*else*/ gmsg.linear.y = 0;
      gmsg.linear.z = vz;
      gmsg.angular.x = 0;
      gmsg.angular.y = 0;
      gmsg.angular.z = vy;
      flag = false;
      count++;
      // subCount++;
      t = 0;
      lost = false;
    }
    else if(enterance){
      gmsg.linear.x = 0.6;
      gmsg.linear.y = 0;
      gmsg.linear.z = 0;
      gmsg.angular.x = 0;
      gmsg.angular.y = 0;
      gmsg.angular.z = 0;
      flag = false;
      subCount++;
      lost = false;
      t = 0;
      count=0;
    }
    // else if(t<10 && !flag){
    //   ++t;
    //   gmsg.linear.x = 0;
    //   if(vy>0.75) gmsg.linear.y = -vy;
    //   else gmsg.linear.y = 0;
    //   gmsg.linear.z = -(0.5*vz);
    //   gmsg.angular.x = 0;
    //   gmsg.angular.y = 0;
    //   gmsg.angular.z = 0.2*(-vy);
    // }
    else {
      gmsg.linear.x = 0;
      gmsg.linear.y = 0.0;
      gmsg.linear.z = 0.0;
      gmsg.angular.x = 0;
      gmsg.angular.y = 0;
      gmsg.angular.z = 0.0;
      staticIt++;
      if(staticIt>=10) lost = true;
      count=0;
    }
    if(subCount>=80) enterance = false;

    cout<<"dyncon published data\tgmsg.linear.y:"<<gmsg.linear.y<<"\tgmsg.linear.z:\t"<<gmsg.linear.z<<endl;

    bmsg.lost = lost;

    pub.publish(gmsg);
    pubBack.publish(bmsg);
    ros::spinOnce();
    loop_rate.sleep();
    // ++count;
  }
  gmsg.linear.x = 0;
  gmsg.linear.y = 0.0;
  gmsg.linear.z = 0.0;
  gmsg.angular.x = 0;
  gmsg.angular.y = 0;
  gmsg.angular.z = 0.0;
  pub.publish(gmsg);
  return 0;
}
