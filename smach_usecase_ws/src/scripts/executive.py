#!/usr/bin/env python

import rospy

import threading

import smach

from smach_ros import ServiceState, IntrospectionServer

from smach import StateMachine

import std_srvs.srv
import turtlesim.srv
import turtle_actionlib.msg


def main():
    rospy.init_node('smach_usecase_executive_03')

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
                    request = turtlesim.srv.SpawnRequest(0.0,0.0,0.0,'turtle2')))

    ########################
    # Add an introspection server to view the smach
    sis = IntrospectionServer('smach_usecase_01', sm_root, '/USE_CASE')
   # Start viewing IntrospectionServer
    sis.start()
    
    outcome = sm_root.execute()

    # Signal ROS shutdown (kill threads in background)
    rospy.spin()

    ########################
    # End viewing IntrospectionServer
    sis.stop()

if __name__ == '__main__':
    main()
