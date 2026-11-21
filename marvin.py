#!/usr/bin/env python3

import board
from edlib.colors import NeoPixelEffects, RED
from adafruit_seesaw import seesaw, neopixel

# def moving_rainbow(strand:neopixel.NeoPixel, num_pixels:int, speed:int=10):
#     """Use list comprehension to create a moving rainbow effect.

#     Requires auto-update.
#     Args:
#         strand: The NeoPixel strand to animate.
#         num_pixels: The number of pixels in the strand.
#         speed: The speed of the moving rainbow effect (lower is faster).
#     """
#     while True:
#         t = time.monotonic() * 1000 / speed
#         strand[:] = [colorwheel( t + i*(255/num_pixels ) ) for i in range(num_pixels)]

# start the rainbow cycle on the NeoPixel strand
i2c = board.I2C()
num_pixels = 35 # Number of pixels driven from the seesaw

print("Init NeoPixel")
ss = seesaw.Seesaw(i2c, addr=0x60)
pixels = neopixel.NeoPixel(ss, 15, num_pixels)

effects = NeoPixelEffects()

try:
    while True:
        pixels.brightness = 0.02
        # effects.rainbow_cycle(pixels, range(num_pixels))
        # effects.moving_rainbow(pixels, num_pixels, speed=100)
        effects.chase(pixels, num_pixels, RED)

except Exception:
    pixels.fill((0,0,0))
    pixels.show()

