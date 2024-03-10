import busio
import displayio
import board
import adafruit_displayio_sh1106

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 64
# create the display and put it to sleep
display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT)
# display.sleep()