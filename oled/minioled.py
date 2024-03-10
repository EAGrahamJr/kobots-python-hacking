#!/usr/bin/env python3

# from board import SCL, SDA
from time import sleep
import busio
import board

# Import the SSD1306 module.
import adafruit_ssd1306


# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# # Set a pixel in the origin 0,0 position.
# display.edbug = True
display.pixel(0, 0, 1)
# # Set a pixel in the middle 64, 16 position.
display.pixel(64, 16, 1)
# # Set a pixel in the opposite 127, 31 position.
display.pixel(127, 31, 1)
display.show()
# display.edbug = False

display.rect(0,0,display.width, display.height, True)
display.show()
sleep(5)
display.text("Hello, world!\nHello, world!\nHello, world!\nHello, world!\nHello, world!\n", 0,0, True)
display.show()
sleep(10)
display.fill(0)
display.show()
