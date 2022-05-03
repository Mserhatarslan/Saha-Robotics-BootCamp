#!/usr/bin/env python
#!/usr/bin/python3
from curses import OK
from sre_constants import SUCCESS
import rospy
import time
from smach import State,StateMachine
from time import sleep
import smach_ros

class PowerOnRobot(State):
    def __init__(self):
        State.__init__(self, outcomes=['succeeded'])

    def execute(self, userdata):
      rospy.loginfo("Powering ON robot...")
      time.sleep(10)
      return 'succeeded'
class ButtonState(State):
    def __init__(self, button_state):
        State.__init__(self, outcomes=['succeeded','aborted'])
        self.button_state=button_state

    def execute(self, userdata):
      if self.button_state == 1:
              return 'succeeded'
      else:
        return 'aborted'       
class F(State):
      def __init__(self):
        State.__init__(self, outcomes=['1','0'], input_keys=['input'], output_keys=[''])
      def execute(self, userdata):
         sleep(1)
         if userdata.input == OK:
            return '1'
class ba(State):
  def __init__(self):
    State.__init__(self, outcomes=['succeed','Fail'], input_keys=['input'], output_keys=[''])
  
  def execute(self, userdata):
    sleep(1)
    if userdata.input == OK:
      return 'succeed'
    else:
      return 'Fail'
class B(State):
  def __init__(self):
    State.__init__(self, outcomes=['1','0'], input_keys=['input'], output_keys=[''])
  def execute(self, userdata):
    sleep(1)
    if userdata.input == OK:
      return '1'
    else:
      return '0'
class ButtonState(State):
    def __init__(self, button_state):
        State.__init__(self, outcomes=['succeeded','aborted'])
        self.button_state=button_state
    def execute(self, userdata):
      time.sleep(10)
      if self.button_state == 1:
              return 'succeeded'
      else:
          return 'aborted'
class Calibration(State):
    def __init__(self, button_state):
        State.__init__(self, outcomes=['succeeded','aborted'])
        self.button_state=button_state
    def execute(self, userdata):
      if self.button_state == 1:
              return 'succeeded'
      else:
          return 'aborted'
class C(State):
  def __init__(self):
    State.__init__(self, outcomes=['1','0','2'], input_keys=['input'], output_keys=[''])
  def execute(self, userdata):
    sleep(3)
    if userdata.input == OK:
      return '1'
    if userdata.input!=OK:
      return '0'
    else:
        return '2'
class D(State):
  def __init__(self):
    State.__init__(self, outcomes=['1','0'], input_keys=['input'], output_keys=[''])
  def execute(self, userdata):
    sleep(3)
    if userdata.input == OK:
      return '1'
    else:
      return '0'
class Initialize(State):
    def __init__(self, button_state):
        State.__init__(self, outcomes=['Succeeed'])
        self.button_state=button_state

    def execute(self, userdata):
      time.sleep(5)

      if self.button_state == 1:
              return 'Succeeed'


class Oscar(State):
    def __init__(self, button_state):
        State.__init__(self, outcomes=['Succeeed', 'Aborted'])
        self.button_state=button_state

    def execute(self, userdata):
      time.sleep(5)

      if self.button_state == 1:
              return 'Succeeed'
      else:
            return 'Aborted'



  
class Fusion(State):
      def __init__(self):
          State.__init__(self, outcomes=['succeed','Fail'], input_keys=['input'], output_keys=[''])
  
      def execute(self, userdata):
        sleep(1)
        if userdata.input == OK:
          return 'succeed'
        else:
          return 'Fail'


class Goal(State):
      def __init__(self):
          State.__init__(self, outcomes=['succeed','Fail'], input_keys=['input'], output_keys=[''])
  
      def execute(self, userdata):
        sleep(1)
        if userdata.input == OK:
          return 'succeed'
        else:
          return 'Fail'
if __name__ == '__main__':

  rospy.init_node('test_fsm', anonymous=True)
  sm = StateMachine(outcomes=['1'])
  sm.userdata.sm_input = OK
  with sm:     
    StateMachine.add('POWER_ON', PowerOnRobot(), transitions={'succeeded':'BUTTON_STATE'})      
    StateMachine.add('System Initialize', Initialize(1), transitions={'Succeeed':'Sensors Offset Value'})             
    StateMachine.add('BUTTON_STATE', ButtonState(1), transitions={'succeeded':'System Initialize','aborted':'BUTTON_STATE'})
    StateMachine.add('Oscar AnR Iterative Control Algorithm', ba(), transitions={'succeed':'Object and Aruco Marker Detection, Orientation','Fail':'Oscar AnR Iterative Control Algorithm'}, remapping={'input':'sm_input','output':'input'})
    StateMachine.add('Reduce Error', B(), transitions={'0':'Imu and Stereo Sensor Fusion','1':'Move To Goal'}, remapping={'input':'sm_input','output':'input'})
    StateMachine.add('Object and Aruco Marker Detection, Orientation', Fusion(), transitions={'succeed':'Imu and Stereo Sensor Fusion','Fail':'System Initialize'}, remapping={'input':'sm_input','output':'input'})
    StateMachine.add('Imu and Stereo Sensor Fusion', C(), transitions={'1':'Reduce Error','0':'Oscar AnR Iterative Control Algorithm','2':'Object and Aruco Marker Detection, Orientation'}, remapping={'input':'sm_input','output':'input'})
    StateMachine.add('Sensors Offset Value', D(), transitions={'0':'System Initialize','1':'Oscar AnR Iterative Control Algorithm'}, remapping={'input':'sm_input','output':'input'})
    StateMachine.add('Move To Goal', Goal(), transitions={'succeed':'Oscar AnR Iterative Control Algorithm','Fail':'Reduce Error'}, remapping={'input':'sm_input','output':'input'})

  sis = smach_ros.IntrospectionServer('model', sm, '/ROBOTIC_ARM')
  sis.start()
  sm.execute()
  rospy.spin()
  sis.stop()
