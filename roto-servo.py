#!/bin/env python3

import time
import board
#import pwmio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

# create a PWMOut object on Pin A2.
#pwm = pwmio.PWMOut(board.D18, duty_cycle=2 ** 15, frequency=50)
i2c = board.I2C()
pca = PCA9685(i2c)
pca.frequency = 50
pwm0 = pca.channels[0]
pwm1 = pca.channels[1]

servo0 = servo.Servo(pwm0, actuation_range=180)
servo0.set_pulse_width_range(500,2400)

servo1 = servo.Servo(pwm1, actuation_range=180)
servo1.set_pulse_width_range(500,2400)

try:
    while True:
        for angle in range(0, 180, 1):  # 0 - 180 degrees, 5 degrees at a time.
            servo0.angle = angle
            if angle % 15 == 0:
                servo1.angle = angle
            time.sleep(1)
        for angle in range(180, 0, -1): # 180 - 0 degrees, 5 degrees at a time.
            servo0.angle = angle
            if angle % 15 == 0:
                servo1.angle = angle
            time.sleep(1)
except:
    servo0.angle = 0
    servo1.angle = 0
