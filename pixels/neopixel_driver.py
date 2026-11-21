#!/usr/bin/env python3

import time
import board
from rainbowio import colorwheel
from adafruit_seesaw import seesaw, neopixel
from edlib.colors import BLUE, CYAN, GREEN, PURPLE, RED, YELLOW

# This little gem was wiring together a WS2818 LED "ring"
# with an Adafruit Neopixel "strip" and using the I2C breakout board

i2c = board.I2C()
num_pixels = 24 # Number of pixels driven from the seesaw
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
        pixels.fill(RED)
        pixels.show()
        # Increase or decrease to change the speed of the solid color change.
        time.sleep(.5)
        pixels.fill(GREEN)
        pixels.show()
        time.sleep(.5)
        pixels.fill(BLUE)
        pixels.show()
        time.sleep(.5)
        print("chase")
        color_chase(RED, CHASE) # Increase the number to slow down the color chase
        color_chase(YELLOW, CHASE)
        color_chase(GREEN, CHASE)
        color_chase(CYAN, CHASE)
        color_chase(BLUE, CHASE)
        color_chase(PURPLE, CHASE)
        print("rainbow")
        rainbow_cycle(0) # Increase the number to slow down the rainbo
except:
    pixels.fill((0,0,0))
    pixels.show()

