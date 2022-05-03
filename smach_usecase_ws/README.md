# TurtleSim-SmachViewer

What is Smach ?

SMACH (pronounced as smash) is a Python-based library that helps us handle complex
robot behaviors. It is a standalone Python tool that can be used to build hierarchical or
concurrent state machines.

SMACH is best useful when
you're able to describe robot behaviors and actions more explicitly (like in our waiter robot
analogy-state machine diagram). SMACH is a simple and wonderful tool to use and define
state machines and is quite powerful when used in combination with ROS actions. The
resultant combination can help us build more sophisticated systems.


The state machine we design or create in smach_ros can be visualized for debugging or
analysis through a tool called SMACH viewer.

LONG STORY SHORT SMACH; 

containers can provide a debugging interface (over ROS) which allows a 
developer to get full introspection into a state machine. 
The SMACH viewer can use this debugging interface to visualize and interact with your state machine.

Main construct of Smach Algorithm 

`First you create a state machine sm` 

 Creating of state machine sm finished

 Create and start the introspection server
` sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')` 
` sis.start()` 

 Execute the state machine
` outcome = sm.execute()` 

 Wait for ctrl-c to stop the application
` rospy.spin()` 
` sis.stop()` 

![image](https://user-images.githubusercontent.com/63358327/166304710-448e1a65-d027-46a7-ae5d-ab763b4ab720.png)









` roslaunch turtle_nodes.launch` 


![image](https://user-images.githubusercontent.com/63358327/166304815-4b2c2eaa-4cbf-4922-a5b2-3d17ea8dd827.png)



` rosrun smach_viewer smach_viewer.py   `


![image](https://user-images.githubusercontent.com/63358327/166304447-50f6a0b1-61da-4a2f-b85f-3102982fe6b4.png)


It initialize the Python Code and simultaneously gives us the ability to control the system


![image](https://user-images.githubusercontent.com/63358327/166305151-8ce7d3ca-e127-424f-9c7a-e1022d353f2e.png)


![image](https://user-images.githubusercontent.com/63358327/166304494-39fb1d49-dcc5-4cff-a8fd-9e79cc18bbd4.png)



![image](https://user-images.githubusercontent.com/63358327/166304532-bea12e62-b6be-4a0d-bd84-0b803dec5890.png)



![image](https://user-images.githubusercontent.com/63358327/166304593-de7c1959-7160-443e-956f-c724e03e7ea3.png)





![image](https://user-images.githubusercontent.com/63358327/166305026-9571bd3f-792a-46d3-b315-ee11487e2131.png)




