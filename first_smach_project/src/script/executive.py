#!/usr/bin/env python
import rospy
import rospkg
import time
from smach import State,StateMachine
from time import sleep
import roslib; 
roslib.load_manifest('smach_usecase')

import smach
def main():
    rospy.init_node('smach_usecase_executive')

    sm_root = smach.StateMachine(outcomes=[])

    with sm_root:
        pass

    outcome = sm_root.execute()

    rospy.spin()

if __name__ == '__main__':
    main()
