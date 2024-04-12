#!/usr/bin/env python3

import time
from adafruit_crickit import crickit

def check_nood():
    from working.manybuttons import SeesawLED
    nood = SeesawLED(crickit.SIGNAL8, crickit.seesaw)

    while True:
        try:
            nood.value = True
            time.sleep(1)
            nood.value = False
            time.sleep(1)
        except KeyboardInterrupt:
            break

    nood.value = False

def under_cabinet():
    from adafruit_seesaw.neopixel import NeoPixel

    num_pixels = 8 # Number of pixels driven from Crickit NeoPixel terminal
    pixels = NeoPixel(crickit.seesaw, 20, num_pixels)

    pixels.fill((255, 142, 91))
    pixels.brightness = 0.5
    # pixels.show()
    input()

    pixels.fill((0,0,0))
    # pixels.show()

# check_nood()
under_cabinet()

