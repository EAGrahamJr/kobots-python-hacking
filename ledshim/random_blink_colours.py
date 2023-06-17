#!/usr/bin/env python

import random
import time

import board
import busio

from adafruit_is31fl3731.led_shim import LedShim
i2c = busio.I2C(board.SCL, board.SDA)

# initial display if you are using Pimoroni LED SHIM
ledshim = LedShim(i2c)

def foo():
    while True:
        for i in range(ledshim.width):
            ledshim.pixelrgb(i, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        time.sleep(0.05)            

try:
    foo()
except:
    ledshim.sleep(True)

