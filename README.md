# Environments
 Ubuntu 18.04 - ROS Melodic
 
![image](https://user-images.githubusercontent.com/63358327/165793266-258bcb0f-0ad8-4b2a-b146-eb2ba040244d.png)
 
 
# Saha-Robotics-BootCamp

Welcome to my document, which serves as an implementation for such things I learned during in the Ros Boot Camp days 🤖

src-> Source Area of Project

build-> Build Area created by Cmake

devel-> Development Area

`mkdir -p ~/reptobot_ws/src`

`cd ~/repbotot_ws/src  ---- > catkin_init_workspace`


Created cmake file in accordance with Ros

Why we use Cmake file?

It is the place where compilation processes are made. 
It is a file that makes both the configuration and parametric redirection 
of the engine running in the back when we press the compile button in 
ide programs such as Visual Studio, Eclipse.

`catkin_create_pkg ilk_paket std_msgs roscpp rospy`

catkin_make, allows the package to be introduced to ros
You can see output of this command like below ;
+++processing catkin_package : 'dedikodu'


We can change effect of line 139 in CmakeLists.txt ( consist of ilk_paket's CmakeLists.txt)
So cpp node files can visible, DECLARE A C++ EXCUTABLE
Has to write node name's in this blank and name's of cpp files
For example ; 
add_executable(hello src/hello.cpp) 
Node name is hello and after that location of this node

![image](https://user-images.githubusercontent.com/63358327/165772579-85464d17-393d-4c92-8c0b-c2d7a9853421.png)


Specify libraries to link a library or executable target against
target_link_libraries(hello ${catkin_LIBRARIES}
This node attached this catkin_libraries 

![image](https://user-images.githubusercontent.com/63358327/165772709-d87d2efb-3cae-4287-93a8-d79aad554319.png)


Adding our C++ file as node and linking the node to catkin library,above change

Output from terminal when we do catkin_make

![image](https://user-images.githubusercontent.com/63358327/165771816-ccac885a-5e2e-428d-92a4-9b01d7781f43.png)


`roscore`

`rosrun dedikodu Cok_Konusan`

`rosrun dedikodu Cok_Dinleyen`

![image](https://user-images.githubusercontent.com/63358327/165776830-ef0b025e-08f4-481e-8bbf-e34066584b64.png)



`rosrun rqt_graph rqt_grapg`

![image](https://user-images.githubusercontent.com/63358327/165776548-c7286001-652c-454a-a63f-1b3355bbd712.png)

![image](https://user-images.githubusercontent.com/63358327/165778407-9ef8e8d3-76a1-4aec-b849-9fc43fe9bcff.png)


`rosrun dedikodu Cok_Konusan __name:= konusan2`

`rosrun dedikodu Cok_Dinleyen __name:= dinleyen2`

`rosrun rqt_graph rqt_grapg`

![image](https://user-images.githubusercontent.com/63358327/165779191-b80a4878-34d7-4309-a109-963459f7c994.png)


![image](https://user-images.githubusercontent.com/63358327/165781978-e2840712-97cc-4265-a44c-24c789caba3b.png)


`roslaunch dedikodu dedikodu.launch`

![image](https://user-images.githubusercontent.com/63358327/165782217-3517218b-fbfb-4c8f-a94e-ef545c490c67.png)

