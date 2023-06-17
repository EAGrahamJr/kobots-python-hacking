#!/usr/bin/env python3

from time import sleep
import board
import busio
from adafruit_is31fl3731.led_shim import LedShim as Display

i2c = busio.I2C(board.SCL, board.SDA)

display = Display(i2c)

# print("Display red for first 10 leds, progressively brighter")
# for x in range(10):
#     display.pixel(x,0, int(255 * (x + 1)/10))
    
print("green all the way up")
for x in range(28):
    display.pixelrgb(x,0,25,0)

# print("red in frame 1")
# for x in range(28):
#     display.pixelrgb(x,100,0,0,frame=1)

# print("blue in frame 2")
# for x in range(28):
#     display.pixelrgb(x,0,0,75,frame=2)

# print("Manual switch to frame 1")
# display.frame = 1
# sleep(1)

# print("Manual switch to frame 2")
# display.frame = 2
# sleep(1)

print("Play")
# display.autoplay(11)
display.frame = 0
# display.fill(color = 10, frame=0)
display.blink(270 * 9)
        
try:
    while True:
        sleep(5)
except:
    print("Stop")
    display.sleep(True)
