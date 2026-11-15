from edlib import rotoservo as rs, rotomotor as rm
#import adafruit_vl6180x
import board
from time import sleep

from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from adafruit_motor.servo import Servo

from adafruit_pca9685 import PCA9685

my_i2c = board.I2C()

pca = PCA9685(my_i2c)
pca.frequency = 50


def hat(channel) -> Servo:
    pwm = pca.channels[channel]
    return Servo(pwm, actuation_range=180)

sx = []
for i in range(0,6):
    sx.append(rs.mg90s(hat(i)))  # a1

solo = rs.mg90s(hat(6))

kit = MotorKit(steppers_microsteps=8)
step1 = rm.RotoStepper(kit.stepper1, delay=0, step_style=stepper.MICROSTEP )

# sensor = adafruit_vl6180x.VL6180X(board.I2C())

def home():
    for s in sx:
        s.angle = 0
    solo.angle = 0


def status():
    st = "Servos: "

    for i in range(0,len(sx)):
        st = st + f"s[{i}] = {sx[i].angle}"

    print(f"{st} -- solo = {solo.angle}")

def up():
    for i in range(5,-1,-1):
        sx[i].angle = 45
    sleep(.05)
    solo.angle = 45

# note: this is pretty shitty
# segs.set_character("H",0).draw()
# segs.set_colon(True/False)
# segs.set_decimal(True/False)
# note: segs.power_on()/off()
