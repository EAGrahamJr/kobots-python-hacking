from edlib import rotoservo as rs
from edlib import rotomotor as rm
from edlib import gpio_stuff as jeep
import board
from digitalio import DigitalInOut,Direction
import pwmio

s1 = rs.mg90s(rs.hat(0))
s2 = rs.mg90s(rs.hat(1))
s3 = rs.mg90s(rs.hat(2))
s4 = rs.mg90s(rs.hat(3))
s5 = rs.mg90s(rs.hat(4))

# step1 = rm.digitalStepper(board.D17,board.D18,board.D10,board.D9)
step1 = rm.digitalStepper(board.D27,board.D21,board.D13,board.D26)

# nood = pwmio.PWMOut(board.D4)
# nood = DigitalInOut(board.D4)
# nood.direction = Direction.OUTPUT
nood = jeep.LED(board.D4)

def home():
    step1.release()
    nood.brightness = 0
    s4.angle = 0
    s2.angle = 0
    s5.angle = 0
    s3.angle = 0
    s1.angle = 0
