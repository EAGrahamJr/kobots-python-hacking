from edlib import rotoservo as rs

s1 = rs.mg90s(rs.hat(0))
s2 = rs.mg90s(rs.hat(1))
s3 = rs.mg90s(rs.hat(2))
s4 = rs.mg90s(rs.hat(3))
s5 = rs.mg90s(rs.hat(4))

def home():
    s4.angle = 0
    s2.angle = 0
    s5.angle = 0
    s3.angle = 0
    s1.angle = 0
