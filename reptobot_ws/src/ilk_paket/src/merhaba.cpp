

#include "ros/ros.h"

int main( int argc, char **argv) /* C++'ın ana fonksiyonu çağırdık */
/* arguman c ve arguman c */

{


    
    
        ros::init(argc, argv, "Merhaba_ROS"); /* dosyayı başlattık */
        ros::NodeHandle nh; /* düğümün açılması kapatılması için kullandık */
        ros::Rate loop_rate(10); /* hız */

        int sayi=0;
        while (ros::ok) /* roscore çalıştığı sürece okey döndürür */
        {
            ROS_INFO_STREAM(" Merhaba Mekatronikciler"<<sayi);  /* bilgilendirici bir mesaj döndürür */

            ros::spinOnce();
            loop_rate.sleep();
            sayi++;

        }
       return 0;
        
        
    
}
