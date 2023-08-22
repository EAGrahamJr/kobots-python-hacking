#!/bin/env python3

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
        current = int(servo.angle)
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

def hat_servo():
    from adafruit_pca9685 import PCA9685
    pca = PCA9685(i2c)
    pca.frequency = 50
    pwm = pca.channels[1]
    return servo.Servo(pwm, actuation_range=180)

def crickit_servo():
    from adafruit_crickit import crickit
    return crickit.servo_4

def run_angles():
    for j in range(5):
        for i in [0,180,90]:
            print(f"Angle = {i}")
            move_servo(myServo, i)
            sleep(2)

# myServo = crickit_servo()
myServo = hat_servo()
# myServo = gpio_servo()
myServo.angle = 90 # just to "put" it somewhere

# print("Using default 750-2250")
# run_angles()

print("Using SG90 500-2400")
myServo.set_pulse_width_range(500,2400)
run_angles()

print("Using extended 500-2500")
myServo.set_pulse_width_range(500,2500)
run_angles()
