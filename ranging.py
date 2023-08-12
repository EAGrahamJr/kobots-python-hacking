#!/bin/env python3

import board
import busio
import adafruit_vl6180x
from time import sleep

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl6180x.VL6180X(i2c)
# sensor.stop_range_continuous()
# print(sensor.range_history_enabled)

# mm = sensor.range
# print(f"Range: {mm}mm")
#lux1 = sensor.read_lux(adafruit_vl6180x.ALS_GAIN_1)
#lux10 = sensor.read_lux(adafruit_vl6180x.ALS_GAIN_10)
#print(f"Lux 1x - {lux1} 10x - {lux10}")

# sensor.start_range_continuous(50)
try:
    while True:
        mm = sensor.range
        print(f"Range: {mm}mm")
        lux1 = sensor.read_lux(adafruit_vl6180x.ALS_GAIN_1)
        lux10 = sensor.read_lux(adafruit_vl6180x.ALS_GAIN_10)
        print(f"Lux 1x - {lux1} 10x - {lux10}")
        sleep(0.1)
except KeyboardInterrupt:
    pass

# sensor.stop_range_continuous()
