from edlib import rotoservo as rs,rotomotor as rm,gpio as jeep
import board
import adafruit_vl6180x
from adafruit_motor.servo import Servo

from adafruit_pca9685 import PCA9685
pca = PCA9685(board.I2C())
pca.frequency = 50

def hat(channel)->Servo:
    pwm = pca.channels[channel]
    return Servo(pwm, actuation_range=180)

s1 = rs.mg90s(hat(0)) # a1
s2 = rs.mg90s(hat(1)) # a2
s3 = rs.mg90s(hat(2)) # twist
s4 = rs.mg90s(hat(3)) # grab
s5 = rs.mg90s(hat(4))

step1 = rm.digitalStepper(board.D27,board.D21,board.D13,board.D26) # ONCE = 4096
step1.speed = .005
step1.release()

nood = jeep.LED(board.D4)
# switch = jeep.Button(board.D23)
sensor = adafruit_vl6180x.VL6180X(board.I2C())

def home():
    nood.brightness = 75
    step1.release()
    s4.angle = 0
    s3.angle = 0

    if s2.angle != 0:
        s2.angle = 30
    s1.angle = 0
    s2.angle = 0

    nood.brightness = 0
