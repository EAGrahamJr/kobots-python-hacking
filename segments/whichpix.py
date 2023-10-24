#!/bin/env python3

from time import sleep
import board
from adafruit_ht16k33 import segments

# i2c = board.STEMMA_I2C()
i2c = board.I2C()
display = segments.Seg14x4(i2c)
display.auto_write = True
# display.brightness = .1
# display.blink_rate = 1

def show_segments():
    for x in range(9):
        # print(f"x {x}")
        for y in range(8):
            # print(f"    y {y}")
            display._pixel(x, y, True)
            # display._pixel(x, y, False)
            sleep(.5)

        # input()
        print("),")
        display.fill(False)

def show_a(x = 0):
    for i in range(7):
        display._pixel(x,i,i != 3)
    display._pixel(x + 4,0, True)

try:
    # display.print(123,0)
    # display._pixel(8,0,True)
    # display._pixel(8,1,True)
    # display.show()
    # display.print("A")
    # display.show()
    # show_segments()
    display._pixel(8,0,True)
    display._pixel(8,1,True)
    print("\nReady to exit")
    input()
except:
    pass

display.fill(False)
display.show()
