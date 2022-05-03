#!/usr/bin/env python 
from turn_robot.srv import TurnRobotService, TurnRobotServiceResponse
from smach_ros import ServiceState
from smach import State
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
        smach.StateMachine.add('TRIGGER_GRIPPER',
                           ServiceState('service_name', GripperSrvRequest(9.0)),
                           transitions={'succeeded':'APPROACH_PLUG'})
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    smach.StateMachine.add('TRIGGER_GRIPPER',
                           ServiceState('service_name',GripperSrv, request = GripperSrv(9.0)), transitions={'succeeded':'APPROACH_PLUG'})
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
