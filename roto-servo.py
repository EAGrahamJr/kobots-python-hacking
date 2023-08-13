#!/bin/env python3

# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
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
pwm = pca.channels[0]

# Create a servo object, my_servo.
servo = servo.Servo(pwm)
servo.set_pulse_width_range(500,2400)

while True:
    for angle in range(0, 180, 1):  # 0 - 180 degrees, 5 degrees at a time.
        servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -1): # 180 - 0 degrees, 5 degrees at a time.
        servo.angle = angle
        time.sleep(0.05)
