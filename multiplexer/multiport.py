#!/usr/bin/python3

# This example shows using TCA9548A to perform a simple scan for connected devices
import board
import adafruit_tca9548a
import adafruit_vcnl4040
import displayio
import adafruit_displayio_ssd1306
import adafruit_ssd1306
from adafruit_display_text import label
from time import sleep
import terminalio

WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 5

i2c = board.I2C()

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# sensor
sensor = adafruit_vcnl4040.VCNL4040(tca[0])
# TODO display causes too muck impedeance on the i2c bus
# display_bus = displayio.I2CDisplay(tca[7], device_address=0x3C)
# display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

# # Draw a label
# text = "Hello World!"
# text_area = label.Label(
#     terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT // 2 - 1
# )

# def show_display():

#     # Make the display context
#     splash = displayio.Group()
#     display.show(splash)

#     color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
#     color_palette = displayio.Palette(1)
#     color_palette[0] = 0xFFFFFF  # White

#     bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
#     splash.append(bg_sprite)

#     # Draw a smaller inner rectangle
#     inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
#     inner_palette = displayio.Palette(1)
#     inner_palette[0] = 0x000000  # Black
#     inner_sprite = displayio.TileGrid(
#         inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
#     )
#     splash.append(inner_sprite)

#     splash.append(text_area)

# show_display()
# sleep(2)

while True:
    try:
        print(f"Proximity: {sensor.proximity}")
        # text_area.text = f"Proximity: {sensor.proximity}"
        sleep(1)
    except KeyboardInterrupt:
        break
