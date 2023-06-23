#!/usr/bin/python3

from armdefs import Arm, _STEPPER_STEPS
from time import sleep

# TODO use for calibration?
import adafruit_vcnl4040

arm = Arm()
midpoint = 90 * 1.4

def full_move():
    try:
        arm.gripper(70)
        arm.shoulder(50)
        arm.gripper(20)
        arm.shoulder_park()
        sleep(2)
        arm.waist(midpoint)
        sleep(2)
        arm.shoulder(50)
        arm.gripper(70)
        sleep(2)
        arm.shoulder_park()
        arm.waist(0)

        # put it back
        fast = .01
        arm.waist(midpoint, rate=fast)
        arm.gripper(70)
        arm.shoulder(50, rate=fast)
        arm.gripper(angle=20)
        arm.shoulder_park(fast)
        arm.waist(0, False, rate=fast)
        arm.shoulder(50, rate=fast)
        arm.gripper(70)
        arm.shoulder_park(fast)

    except KeyboardInterrupt:
        pass

def elbow_bend():
    for i in range(90):
        arm._elbow.angle = i
        sleep(.02)
    for i in range(90,0,-1):
        arm._elbow.angle = i
        sleep(.02)

#elbow_bend()
full_move()
arm.close()

