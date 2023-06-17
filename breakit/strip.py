#!/usr/bin/python3

import board
import adafruit_seesaw.neopixel as np
import adafruit_seesaw.seesaw
from rainbowio import colorwheel
from time import sleep

i2c = board.I2C()
seesaw = adafruit_seesaw.seesaw.Seesaw(i2c,0x60)
strip =  np.NeoPixel(seesaw, 15, 30)

while True:
    try:
        for color in range(255):
            for pixel in range(len(strip)):
                pixel_index = (pixel * 256 // len(strip)) + color * 5
                strip[pixel] = colorwheel(pixel_index & 255)
        strip.show()
        sleep(5)
    except Exception as e:
        print(e)
        break
