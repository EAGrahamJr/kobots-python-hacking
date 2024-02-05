#!/usr/bin/env python3

# from board import SCL, SDA
from time import sleep
import busio
import displayio
import terminalio
import board
from adafruit_display_text import label
import adafruit_displayio_sh1106

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 64
BORDER = 5
display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT)

def og():
    # Make the display context
    splash = displayio.Group()
    display.root_group = splash

    color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF  # White

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    print("Drawing background")
    splash.append(bg_sprite)

    # Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000  # Black
    inner_sprite = displayio.TileGrid(
        inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
    )
    print("Drawing inner")
    splash.append(inner_sprite)

    # Draw a label
    text = "Hello World!"
    text_area = label.Label(
        terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT // 2 - 1
    )
    print("Drawing text")
    splash.append(text_area)

def dots():
    from adafruit_display_shapes.circle import Circle

    group = displayio.Group()

    # Create shapes for the dots
    dot1 = Circle(x0=0, y0=0, r=2, fill=0xFFFFFF)  # Upper left corner
    dot2 = Circle(r=2, x0=display.width // 2, y0=display.height // 2, fill=0xFFFFFF)  # Middle
    dot3 = Circle(r=2, x0=display.width - 1, y0=display.height - 1, fill=0xFFFFFF)  # Lower right corner

    # Add the shapes to the group
    group.append(dot1)
    group.append(dot2)
    group.append(dot3)

    # Show the group on the display
    display.show(group)

# og()
# dots()

while True:
    try:
        sleep(1)
    except KeyboardInterrupt:
        break
