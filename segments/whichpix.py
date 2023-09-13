#!/bin/env python3

from time import sleep
import board
from adafruit_ht16k33 import segments
import adafruit_vl6180x

# i2c = board.STEMMA_I2C()
i2c = board.I2C()
display = segments.Seg14x4(i2c)
display.auto_write = False
# display.brightness = .1
# display.blink_rate = 1
sensor = adafruit_vl6180x.VL6180X(i2c)

sensor_tripped = False

def sensor_trip():
    global sensor_tripped

    sensor_waiting = True
    while sensor_waiting:
        sleep(.25)

        reading = sensor.range
        if reading < 100:
            if not sensor_tripped:
                sensor_waiting = False
            sensor_tripped = True
        else:
            sensor_tripped = False

def show_segments():
    for x in range(9):
        print(f"x {x}")
        for y in range(8):
            # print(f"    y {y}")
            display._pixel(x, y, True)
            # display._pixel(x, y, False)
            sleep(.5)

        sensor_trip()
        display.fill(False)

def show_a(x = 0):
    for i in range(7):
        display._pixel(x,i,i != 3)
    display._pixel(x + 4,0, True)

try:
    # display.print(123,0)
    display._pixel(8,0,True)
    # display._pixel(8,1,True)
    display.show()
    sensor_trip()
    # display.print("A")
    # display.show()
    # sensor_trip()
except:
    pass

display.fill(False)
display.show()
