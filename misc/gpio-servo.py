#!/bin/env python
from time import sleep
import board
import pwmio
from adafruit_motor import servo

servo_pin = pwmio.PWMOut(board.D18, frequency=50)
servo = servo.Servo(servo_pin, min_pulse=500, max_pulse=2400)

servo.angle = 60
sleep(.5)
servo.angle = 120
sleep(.5)
servo.angle = 180
sleep(.5)
servo.angle = 0

