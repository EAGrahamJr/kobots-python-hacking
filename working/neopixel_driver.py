#!/usr/bin/python3

import time
import board
from rainbowio import colorwheel
from adafruit_seesaw import seesaw, neopixel
from edstuff import _BLUE, _CYAN, _GREEN, _PURPLE, _RED, _YELLOW

# This little gem was wiring together a WS2818 LED "ring"
# with an Adafruit Neopixel "strip" and using the I2C breakout board

i2c = board.I2C()
num_pixels = 38 # Number of pixels driven from the seesaw
# The following line sets up a NeoPixel strip on Seesaw pin 15 for I2C breakout

print("Init NeoPixel")
ss = seesaw.Seesaw(i2c, addr=0x60)
pixels = neopixel.NeoPixel(ss, 15, num_pixels)

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
        time.sleep(0.5)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
    pixels.show()


CHASE = 0.02
try:
    pixels.brightness = 0.1
    pixels.show()
    while True:
        print("fill")
        pixels.fill(_RED)
        pixels.show()
        # Increase or decrease to change the speed of the solid color change.
        time.sleep(.5)
        pixels.fill(_GREEN)
        pixels.show()
        time.sleep(.5)
        pixels.fill(_BLUE)
        pixels.show()
        time.sleep(.5)
        print("chase")
        color_chase(_RED, CHASE) # Increase the number to slow down the color chase
        color_chase(_YELLOW, CHASE)
        color_chase(_GREEN, CHASE)
        color_chase(_CYAN, CHASE)
        color_chase(_BLUE, CHASE)
        color_chase(_PURPLE, CHASE)
        print("rainbow")
        rainbow_cycle(0) # Increase the number to slow down the rainbo
except:
    pixels.fill((0,0,0))
    pixels.show()

