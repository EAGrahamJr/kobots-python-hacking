from edlib import colors as c
from edlib import rotoservo as rs
from edlib import rotomotor as rm
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel
import board
import adafruit_vcnl4040

i2c = board.I2C()

# servos
s1 = rs.mg90s(rs.crickit(1))
s2 = rs.mg90s(rs.crickit(2))
s3 = rs.mg90s(rs.crickit(3))
s4 = rs.mg90s(rs.crickit(4))

# steppers
step1 = rm.RotoStepper(crickit.drive_stepper_motor) # ONCE = 2048
step1.speed = .01
step1.release()
# note: currently takes about 16000 steps to move the scrissor up and down
step2 = rm.RotoStepper(crickit.stepper_motor)     # ONCE = 400
step2.release()

# NeoPixel strand
# crickit.init_neopixel(8, brightness=.1)
# strand = crickit.neopixel
strand = NeoPixel(crickit.seesaw, 20, 8)
strand.fill(c.BLACK)
# status = crickit.onboard_pixel
#status = NeoPixel(crickit.seesaw, 27, 1)

sensor = adafruit_vcnl4040.VCNL4040(i2c)

def home():
    step1.release()
    step2.release()
    s2.angle = 0
    s3.angle = 0
    s4.angle = 0
    s1.angle = 0

    strand.fill(c.BLACK)
    # status.fill(c.GREEN)
    # status.brightness = .05
