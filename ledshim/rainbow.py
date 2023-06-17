#!/usr/bin/env python

import colorsys
import time
import board
import busio

from adafruit_is31fl3731.led_shim import LedShim
i2c = busio.I2C(board.SCL, board.SDA)

# initial display if you are using Pimoroni LED SHIM
ledshim = LedShim(i2c)

spacing = 360.0 / 16.0
hue = 0

# ledshim.set_clear_on_exit()
# ledshim.set_brightness(0.8)

try:
    while True:
        hue = int(time.time() * 100) % 360
        for x in range(28):
            offset = x * spacing
            h = ((hue + offset) % 360) / 360.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            ledshim.pixelrgb(x, r, g, b)

        # ledshim.show()
        time.sleep(0.0001)
except:
    ledshim.sleep(True)
