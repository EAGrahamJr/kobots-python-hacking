#!/usr/bin/python3

# This example shows using TCA9548A to perform a simple scan for connected devices
import board
import adafruit_tca9548a
import adafruit_vcnl4040
import adafruit_ssd1306
from adafruit_display_text import label
from time import sleep
from PIL import Image, ImageDraw, ImageFont

WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 5

i2c = board.I2C()

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# sensor = adafruit_vcnl4040.VCNL4040(i2c)
sensor = adafruit_vcnl4040.VCNL4040(tca[0])
# display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)
# display1 = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, tca[7], addr=0x3C)
# display2 = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, tca[6], addr=0x3C)

# Create blank image for drawing.
image1 = Image.new("1", (WIDTH, HEIGHT))
draw1 = ImageDraw.Draw(image1)
image2 = Image.new("1", (WIDTH, HEIGHT))
draw2 = ImageDraw.Draw(image2)

# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

def clear_image():
    draw1.rectangle((0,0,WIDTH,HEIGHT), fill=0)
    display1.show()
    draw2.rectangle((0,0,WIDTH,HEIGHT), fill=0)
    display2.show()

# clear_image()

# Draw the text
# draw1.text((0, 0), "Hello!", font=font2, fill=255)
# draw2.text((0, 17), "Hello!", font=font2, fill=255)

# Display image -- cheating a bit
def show_image():
    display1.image(image1)
    display1.show()
    display2.image(image2)
    display2.show()

#show_image()
#sleep(2)
#clear_image()

def do_it():
    # print(f"reading =============================================================")
    reading = f"********* Lux: {sensor.lux}"
    print(reading)
#    print("display on 7 ===========================================================")
#    draw1.text((0, 0),reading, font=font2, fill=255)
#    display1.image(image1)
#    display1.show()
#    print("display on 6 ===========================================================")
#    draw2.text((0,0), f"Prox: {sensor.proximity}", font=font2, fill=255)
#    display2.image(image2)
#    display2.show()

while True:
    try:
        # clear_image()
        do_it()
        sleep(5)
    except KeyboardInterrupt:
        break
# do_it()
# sleep(5)
# clear_image()
