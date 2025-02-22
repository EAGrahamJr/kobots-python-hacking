from edlib import colors as c,rotoservo as rs,rotomotor as rm,seesaw_util as su
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel
import board
import adafruit_vcnl4040
import adafruit_vl6180x
from adafruit_motor import stepper

i2c = board.I2C()

# servos
s1 = rs.mg90s(crickit.servo_1)
s2 = rs.sg90(crickit.servo_2)
s3 = rs.mg90s(crickit.servo_3)
s4 = rs.mg90s(crickit.servo_4)

# steppers
step1 = rm.RotoStepper(crickit.drive_stepper_motor, step_size=stepper.INTERLEAVE) # ONCE = 4096
step1.speed = .005
step1.release()

step2 = rm.RotoStepper(crickit.stepper_motor, step_size=stepper.INTERLEAVE) # ONCE = 4096
step2.speed = .005
step2.release()

# NeoPixel strand
strand = NeoPixel(crickit.seesaw, 20, 8)
strand.fill(c.BLACK)

# proximity sensor
prox = adafruit_vcnl4040.VCNL4040(i2c)
# tof sensor
toffle = adafruit_vl6180x.VL6180X(i2c)

# digital input - limit switch on thermometer
t_switch = su.Button(crickit.SIGNAL1, crickit.seesaw)

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
