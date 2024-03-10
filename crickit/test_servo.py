import time
from adafruit_crickit import crickit

servo = crickit.servo_2

print("\nSet PWM")
servo.set_pulse_width_range(500,2400)

print("\nMoving servo to 90")
servo.angle = 90 # middle
time.sleep(1)
print("\nMoving servo to 180")
servo.angle = 180 # left
time.sleep(1)
print("\nMoving servo to 0")
servo.angle = 0 # right
