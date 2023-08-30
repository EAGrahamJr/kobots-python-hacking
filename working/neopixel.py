#!/usr/bin/python3

import time
from rainbowio import colorwheel
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel

num_pixels = 8 # Number of pixels driven from Crickit NeoPixel terminal
# The following line sets up a NeoPixel strip on Seesaw pin 20 for Feather

print("Init NeoPixel")
pixels = NeoPixel(crickit.seesaw, 20, num_pixels)

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

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

CHASE = 0.02
try:
    pixels.brightness = 0.01
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

