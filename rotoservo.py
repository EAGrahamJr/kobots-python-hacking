#!/bin/env python3

"""
A "test" to determine if the SG90 is different than the MG90 or
is it the controllers.

FYI, it's the servos.
"""

from time import sleep
import board
from adafruit_motor import servo

i2c = board.I2C()

def move_servo(servo, angle: float, rate: float = 0.015):
        """Move a servo to a certain angle.

        Args:
            servo (Servo): the servo
            angle (float): where to move to
            rate (float): pause between steps in seconds or fractions thereof
        """
        current = round(servo.angle)
        if angle == current:
            return
        if angle > current:
            delta = 1
        else:
            delta = -1

        for i in range(current, angle, delta):
            servo.angle = i
            sleep(rate)

        servo.angle = angle

def gpio_servo():
    import pwmio
    pwm = pwmio.PWMOut(board.D18, duty_cycle=2 ** 15, frequency=50)
    return servo.Servo(pwm, actuation_range=180)

def hat_servo(channel:int = 0):
    from adafruit_pca9685 import PCA9685
    pca = PCA9685(i2c)
    pca.frequency = 50
    pwm = pca.channels[channel]
    return servo.Servo(pwm, actuation_range=180)

def crickit_servo():
    from adafruit_crickit import crickit
    return crickit.servo_4

def run_angles(servo):
    for j in range(5):
        for i in [0,180,90]:
            print(f"Angle = {i}")
            move_servo(servo, i)
            sleep(2)

# sv = crickit_servo()
sv = hat_servo(0)
# sv = gpio_servo()
# sv.angle = 0 # just to "put" it somewhere

# print("Using default 750-2250")
# run_angles()

# print("Using SG90 500-2400")
# sv.set_pulse_width_range(500,2400)
# run_angles()

print("Using extended 500-2500")
sv.set_pulse_width_range(500,2500)
run_angles(sv)

# reset for Servomatic "home"
# move_servo(sv, 90)
