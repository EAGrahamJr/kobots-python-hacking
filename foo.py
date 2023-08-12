#!/usr/bin/python3

from time import sleep
from arm import Arm, _SHOULDER_UP

# TODO use for calibration?
import adafruit_vcnl4040

arm = Arm()
midpoint = 90 * 1.4

def full_move():
    try:
        arm.gripper(70)
        arm.shoulder(50)
        arm.gripper(20)
        arm.shoulder(_SHOULDER_UP)
        sleep(2)
        arm.waist(midpoint)
        sleep(2)
        arm.shoulder(50)
        arm.gripper(70)
        sleep(2)
        arm.shoulder(_SHOULDER_UP)
        arm.waist(0)

        # put it back
        fast = .01
        arm.waist(midpoint, rate=fast)
        arm.gripper(70)
        arm.shoulder(50, rate=fast)
        arm.gripper(angle=20)
        arm.shoulder(_SHOULDER_UP, rate=fast)
        arm.waist(0, False, rate=fast)
        arm.shoulder(50, rate=fast)
        arm.gripper(70)
        arm.shoulder(_SHOULDER_UP, rate=fast)

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

