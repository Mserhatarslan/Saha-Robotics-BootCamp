#!/usr/bin/env python

import rospy

import threading

import smach
from math import sqrt, pow
from smach_ros import ServiceState, SimpleActionState, IntrospectionServer,set_preempt_handler, MonitorState

from smach import StateMachine, Concurrence

import std_srvs.srv
import turtlesim.srv
import turtlesim.msg
import turtle_actionlib.msg


def main():
    rospy.init_node('executive_new2')

    # Construct static goals
    polygon_big = turtle_actionlib.msg.ShapeGoal(edges = 11, radius = 4.0)
    polygon_small = turtle_actionlib.msg.ShapeGoal(edges = 6, radius = 0.5) 

    # Create a SMACH state machine
    sm_root = StateMachine(outcomes=['succeeded','aborted','preempted'])

    # Open the container
    with sm_root:
		# Reset turtlesim
		StateMachine.add('RESET',
                ServiceState('reset', std_srvs.srv.Empty),
                {'succeeded':'SPAWN'})

        # Create a second turtle
		StateMachine.add('SPAWN',
						 ServiceState('spawn', turtlesim.srv.Spawn,
									  request=turtlesim.srv.SpawnRequest(0.0, 0.0, 0.0, 'turtle2')),
						 {'succeeded': 'TELEPORT1'})
        # Teleport turtle 1
		StateMachine.add('TELEPORT1',
						 ServiceState('turtle1/teleport_absolute',
						 turtlesim.srv.TeleportAbsolute,
						 request = turtlesim.srv.TeleportAbsoluteRequest(5.0,1.0,0.0)),
						 {'succeeded':'DRAW_SHAPES'})

		shape_cc = Concurrence(outcomes=['succeeded','aborted','preempted'],
							   default_outcome='aborted',
							   outcome_map ={'succeeded':{'BIG':'succeeded','SMALL':'succeeded'}})
	
		StateMachine.add('DRAW_SHAPES',shape_cc)
	
		with shape_cc:
			Concurrence.add("BIG", 
							SimpleActionState('turtle_shape1', turtle_actionlib.msg.ShapeAction,
				            goal = polygon_big))

			# Draw a small polygon with the second turtle
			small_shape_sm = StateMachine( outcomes=['succeeded', 'aborted', 'preempted'] )
			Concurrence.add('SMALL', small_shape_sm)

			with small_shape_sm:
		        # Teleport turtle 2
				StateMachine.add('TELEPORT2',
		                    	ServiceState('turtle2/teleport_absolute', turtlesim.srv.TeleportAbsolute,
		                        request = turtlesim.srv.TeleportAbsoluteRequest(9.0,5.0,0.0)),
		                    	{'succeeded':'DRAW_WITH_MONITOR'})


				draw_monitor_cc = Concurrence(
								['succeeded','aborted','preempted','interrupted'],
								'aborted',
								child_termination_cb = lambda so: True,
								outcome_map = {
									'succeeded':{'DRAW':'succeeded'},
									'preempted':{'DRAW':'preempted','MONITOR':'preempted'},
									'interrupted':{'MONITOR':'invalid'}})
		   
				StateMachine.add('DRAW_WITH_MONITOR',
		                    	draw_monitor_cc,
		                    	{'interrupted':'WAIT_FOR_CLEAR'})

				with draw_monitor_cc:

					Concurrence.add("DRAW", 
									SimpleActionState('turtle_shape2', turtle_actionlib.msg.ShapeAction,
						    		goal = polygon_small))
					def turtle_far_away(ud, msg):
						"""Returns True while turtle pose in msg is at least 1 unit away from (9,5)"""
						if sqrt(pow(msg.x-9.0,2) + pow(msg.y-5.0,2)) > 2.0:
							return True
						return False
					Concurrence.add('MONITOR',
									MonitorState('/turtle1/pose',turtlesim.msg.Pose,
									cond_cb = turtle_far_away))
		        
				StateMachine.add('WAIT_FOR_CLEAR',
		                    		MonitorState('/turtle1/pose',turtlesim.msg.Pose,
		                        	cond_cb = lambda ud,msg: not turtle_far_away(ud,msg)),
		                    		{'valid':'WAIT_FOR_CLEAR','invalid':'TELEPORT2'})

    # Attach a SMACH introspection server
    sis = IntrospectionServer('smach_usecase_01', sm_root, '/USE_CASE')
    sis.start()
    
    # Set preempt handler
    set_preempt_handler(sm_root)

    # Execute SMACH tree in a separate thread so that we can ctrl-c the script
    smach_thread = threading.Thread(target = sm_root.execute)
    smach_thread.start()

    # Signal ROS shutdown (kill threads in background)
    rospy.spin()

    sis.stop()

if __name__ == '__main__':
    main()
