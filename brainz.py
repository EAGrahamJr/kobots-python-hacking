from edlib import colors as c, rotoservo as rs, rotomotor as rm, seesaw_util as su
from adafruit_crickit import crickit
import board

# import adafruit_vcnl4040
import adafruit_vl6180x
from adafruit_motor import stepper
from time import sleep


def np_init():
    # NeoPixel strand - must be re-initialized after every
    # "on-board" call because the CRICKIT switches buffer
    # addresses and lengths
    crickit.init_neopixel(16)
    crickit.neopixel.fill(c.BLACK)
    sleep(0.1)


i2c = board.I2C()

# servos
s1 = rs.mg996r(crickit.servo_1)
s2 = rs.mg996r(crickit.servo_2)
s3 = rs.mg90s(crickit.servo_3)
s4 = rs.mg90s(crickit.servo_4)

# steppers
step1 = rm.RotoStepper(
    crickit.drive_stepper_motor  # , step_size=stepper.INTERLEAVE
)  # ONCE = 4096
step1.speed = 0.005
step1.release()

step2 = rm.RotoStepper(
    crickit.stepper_motor  # , step_size=stepper.INTERLEAVE
)  # ONCE = 4096
step2.speed = 0.002
step2.release()

crickit.onboard_pixel.fill(c.BLACK)
sleep(0.1)
np_init()

# digital port - configured for "out"
# nood_port = su.LED(crickit.SIGNAL1,crickit.seesaw)

# proximity sensor
# prox = adafruit_vcnl4040.VCNL4040(i2c)
# tof sensor
toffle = adafruit_vl6180x.VL6180X(i2c)

# digital input - limit switch on thermometer
# t_switch = su.Button(crickit.SIGNAL1, crickit.seesaw)


def reset():
    s4.angle = 0

    while toffle.range >= 5:
        step1.forward(5)


def home():
    # reset()
    step1.release()
    step2.release()
    s1.angle = 0
    s4.angle = 0
    s3.angle = 0
    s2.angle = 0

    crickit.onboard_pixel.fill(c.BLACK)
    np_init()
