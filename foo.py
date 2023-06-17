#!/usr/bin/python3

from armdefs import Arm, _STEPPER_STEPS
from time import sleep

arm = Arm()
steps = int(_STEPPER_STEPS/4)

def full_move():
    try:
        arm.gripper_open()
        arm.shoulder_move(50)
        arm.gripper.angle = 20
        arm.shoulder_park()
        sleep(2)
        arm.waist_move(steps)
        sleep(2)
        arm.shoulder_move(50)
        arm.gripper_open()
        sleep(2)
        arm.shoulder_park()
        arm.waist_move(steps, False)
    
        # put it back
        fast = .01
        arm.waist_move(steps, rate=fast)
        arm.gripper_open()
        arm.shoulder_move(50, rate=fast)
        arm.gripper.angle = 20
        arm.shoulder_park(fast)
        arm.waist_move(steps, False, rate=fast)
        arm.shoulder_move(50, rate=fast)
        arm.gripper_open()
        arm.shoulder_park(fast)
        
    except KeyboardInterrupt:
        pass

def elbow_bend():
    for i in range(90):
        arm.elbow.angle = i
        sleep(.02)
    for i in range(90,0,-1):
        arm.elbow.angle = i
        sleep(.02)

elbow_bend()
arm.close()

