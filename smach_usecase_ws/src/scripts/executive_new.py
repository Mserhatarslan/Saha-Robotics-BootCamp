from smach_ros import ServiceState
import roslib
from curses import OK
from sre_constants import SUCCESS
import time
from smach import State,StateMachine
from time import sleep
import smach_ros

from smach import State,StateMachine
import smach_ros
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
        smach.StateMachine.add('TRIGGER_GRIPPER',
                            ServiceState('service_name',
                             GripperSrv),
                            transitions={'succeeded':'APPROACH_PLUG'})
        sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    smach.StateMachine.add('TRIGGER_GRIPPER',
                           ServiceState('service_name',
                                        GripperSrv,
                                        request = GripperSrv(9.0)),
                           transitions={'succeeded':'APPROACH_PLUG'})
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    smach.StateMachine.add('TRIGGER_GRIPPER',
                           ServiceState('service_name',
                                        GripperSrv,
                                        request_slots = ['max_effort',
                                                         'position']),
                           transitions={'succeeded':'APPROACH_PLUG'})
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:

    def gripper_request_cb(userdata, request):
       gripper_request = GripperSrv().Request
       gripper_request.position.x = 2.0
       gripper_request.max_effort = userdata.gripper_input
       return gripper_request

    smach.StateMachine.add('TRIGGER_GRIPPER',
                           ServiceState('service_name',
                                        GripperSrv,
                                        request_cb = gripper_request_cb),
                           transitions={'succeeded':'APPROACH_PLUG'})

