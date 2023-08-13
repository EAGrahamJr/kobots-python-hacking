#!/usr/bin/python3

from datetime import datetime
from time import sleep
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel

num_pixels = 30 # Number of pixels driven from Crickit NeoPixel terminal
# The following line sets up a NeoPixel strip on Seesaw pin 20 for Feather

crickit.seesaw.edbug = False

print("Init Strip Manager")
pixels = NeoPixel(crickit.seesaw, 20, num_pixels)
pixels.auto_write = True
pixels.brightness = 0.05

_RED = (255, 0, 0)
_PURPLE = (180, 0, 255)
_BLACK = (0,0,0)

pixels.fill(_RED)
sleep(5)

last_color = None
while True:
    try:
        now = datetime.now()
        
        if now.hour < 8 or now.hour >= 23:
            color = _BLACK
            bright = 0
        elif now.hour < 21:
            color = _PURPLE
            bright = 0.1
        else:
            color = _RED
            bright = 0.05
        
        if last_color != color:
            last_color = color
            pixels.brightness = bright
            pixels.fill(color)
    except Exception as e:
        print(e)
    sleep(60)
