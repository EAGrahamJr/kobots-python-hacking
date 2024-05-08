from edlib import rotoservo as rs
from edlib import rotomotor as rm
from adafruit_crickit import crickit

s1 = rs.mg90s(rs.crickit(1))
s2 = rs.mg90s(rs.crickit(2))
s3 = rs.mg90s(rs.crickit(3))
s4 = rs.mg90s(rs.crickit(4))

step1 = rm.RotoStepper(crickit.drive_stepper_motor) # ONCE = 2048
# note: currently takes about 16000 steps to move the scrissor up and down
step2 = rm.RotoStepper(crickit.stepper_motor)     # ONCE = 400

def home():
    s2.angle = 0
    s3.angle = 0
    s4.angle = 0
    s1.angle = 0
