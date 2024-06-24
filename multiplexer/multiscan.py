#!/usr/bin/env python3

# This example shows using TCA9548A to perform a simple scan for connected devices
import board
import adafruit_tca9548a
from time import sleep

# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# !!!!!NOTE!!!!! this particular multiplexer has a "bad" channel 2 and will "lock" the I2C bus
while True:
    try:
        print("2 second sleep")
        sleep(2)
        for channel in range(8):
            if channel != 2:
                if tca[channel].try_lock():
                    print("Channel {}:".format(channel), end="")
                    addresses = tca[channel].scan()
                    print([hex(address) for address in addresses if address != 0x70])
                    tca[channel].unlock()
    except KeyboardInterrupt:
        break
    except Exception as e:
        print("Error: ",e)
