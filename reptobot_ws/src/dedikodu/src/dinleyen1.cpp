#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
void konusmaCallback( const std_msgs::String::ConstPtr& msg);
int main( int argc, char **argv)
{
    ros::init(argc,argv,"Cok_Dinleyen");
    ros::NodeHandle nh;
    ros::Subscriber sub_dinleyen;
    sub_dinleyen = nh.subscribe("konusan_teyze", 1000,konusmaCallback);
    ros::spin();
    return 0;    
}

void konusmaCallback( const std_msgs::String::ConstPtr& msg)
{
    ROS_INFO( "Teyze ne dediğini duydum %s", msg->data.c_str());
}
