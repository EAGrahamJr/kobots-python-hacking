#!/usr/bin/env python3

import time
from adafruit_crickit import crickit
from adafruit_motor import stepper
from adafruit_motor.stepper import StepperMotor

print("Stepper motor demo!")

def runIt(motor:StepperMotor, delay:float = 0.02, steps:int = 200):
    print("Forward---------------------------------")
    for i in range(steps):
        motor.onestep(direction=stepper.FORWARD)
        time.sleep(delay)
    print("Backward--------------------------------")
    for i in range(steps):
        motor.onestep(direction=stepper.BACKWARD)
        time.sleep(delay)

    print("Double-step-----------------------------")
    for i in range(steps):
        motor.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        time.sleep(delay)
    for i in range(steps):
        motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(delay)

    print("Interleave------------------------------")
    for i in range(steps * 2):
        motor.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
        time.sleep(delay)
    for i in range(steps * 2):
        motor.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
        time.sleep(delay)

    # print("Microstep-------------------------------")
    # for i in range(steps * 10):
    #     motor.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)
    #     time.sleep(delay)
    # for i in range(steps * 10):
    #     motor.onestep(direction=stepper.BACKWARD, style=stepper.MICROSTEP)
    #     time.sleep(delay)

crickit.seesaw.edbug = False

motor = None
delay = None
ONCE = 1

picked = int(input("Which stepper (1=drive, 2=stepper, 0=exit: "))

if picked == 0:
    exit
# Unipolar stepper
if picked == 1:
    print("Picked drive")
    motor = crickit.drive_stepper_motor
    ONCE = 2048
    delay = .001
# Bipolar stepper
if picked == 2:
    print("Picked stepper")
    motor = crickit.stepper_motor
    ONCE = 200
    delay = .02

# try:
#     # Demo/debug things
#     # crickit.seesaw.edbug = True
#     # runIt(motor, steps=4)

#     # single rotation
#     for i in range(50):
#         motor.onestep(direction=stepper.FORWARD)
#         time.sleep(delay)
# except Exception:
#     pass

while(True):
    num = int(input("Enter an integer (0 exits): "))
    if num == 0:
        break

    if num > 0:
        dir = stepper.FORWARD
    else:
        dir = stepper.BACKWARD

    for i in range(abs(num)):
        motor.onestep(direction=dir)
        time.sleep(delay)

crickit.seesaw.edbug = False
motor.release()
