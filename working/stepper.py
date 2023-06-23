#!/usr/bin/python3

import time
from adafruit_crickit import crickit
from adafruit_motor import stepper
from adafruit_motor.stepper import StepperMotor

print("Stepper motor demo!")

def motor_motor(motor:StepperMotor):
    print("Forward---------------------------------")
    motor.onestep(direction=stepper.FORWARD)
    motor.onestep(direction=stepper.FORWARD)
    motor.onestep(direction=stepper.FORWARD)

    print("Backward--------------------------------")
    motor.onestep(direction=stepper.BACKWARD)
    motor.onestep(direction=stepper.BACKWARD)
    motor.onestep(direction=stepper.BACKWARD)
    motor.onestep(direction=stepper.BACKWARD)

    print("Double-step-----------------------------")
    motor.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
    motor.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
    motor.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
    motor.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)

    print("Interleave------------------------------")
    motor.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
    motor.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
    motor.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
    motor.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)

    print("Release---------------------------------")
    motor.release()


def keep_swingin(motor, delay:float = 0.02):
    try:
        while True:
            print("Single step")
            for i in range(200):
                motor.onestep(direction=stepper.FORWARD)
                time.sleep(delay)
            for i in range(200):
                motor.onestep(direction=stepper.BACKWARD)
                time.sleep(delay)
            print("Double step")
            for i in range(200):
                motor.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
                time.sleep(delay)
            for i in range(200):
                motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
                time.sleep(delay)
            print("Interleave step")
            for i in range(200):
                motor.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
                time.sleep(delay)
            for i in range(200):
                motor.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
                time.sleep(delay)
            # print("Microstepping")
            # for i in range(2000):
            #     motor.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)
            #     time.sleep(delay)
            # for i in range(2000):
            #     motor.onestep(direction=stepper.BACKWARD, style=stepper.MICROSTEP)
            #     time.sleep(delay)

    except Exception:
	    motor.release()

crickit.seesaw.edbug = False
# stepper_motor = crickit.drive_stepper_motor
# for i in range(2048):
#    stepper_motor.onestep(direction=stepper.FORWARD)
#    time.sleep(delay)
# stepper_motor.release()

# keep_swingin(crickit.drive_stepper_motor)
# keep_swingin(crickit.stepper_motor)

# motor_motor(crickit.drive_stepper_motor)
# motor_motor(crickit.stepper_motor)

# ratio 1:1.29
for i in range(258):
    crickit.stepper_motor.onestep(direction=stepper.FORWARD)
    time.sleep(.02)
crickit.stepper_motor.release()
