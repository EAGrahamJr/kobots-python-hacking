from edlib import rotoservo as rs
from edlib import rotomotor as rm
import board
from digitalio import DigitalInOut,Direction
import pwmio
from adafruit_motor import stepper
import adafruit_vl6180x

s1 = rs.mg90s(rs.hat(0)) # a1
s2 = rs.mg90s(rs.hat(1)) # a2
s3 = rs.mg90s(rs.hat(2)) # twist
s4 = rs.mg90s(rs.hat(3)) # grab
s5 = rs.mg90s(rs.hat(4))

# step1 = rm.digitalStepper(board.D17,board.D18,board.D10,board.D9)
step1 = rm.digitalStepper(board.D27,board.D21,board.D13,board.D26) # ONCE = 4096
step1.speed = .005
step1.release()

# nood = pwmio.PWMOut(board.D4)
# nood = DigitalInOut(board.D4)
# nood.direction = Direction.OUTPUT
nood = jeep.LED(board.D4)
#switch = jeep.Button(board.D23)
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
