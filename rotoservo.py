"""
Stuff for servos, including a "smooth move" just to keep things from going off the rails.

Uset to be a physical test thingie.
"""

from time import sleep
import board
from adafruit_motor.servo import Servo

def move_servo(servo:Servo, angle: float, rate: float = 0.025):
        """Move a servo to a certain angle.

        Args:
            servo (Servo): the servo
            angle (float): where to move to
            rate (float): pause between steps in seconds or fractions thereof
        """
        current = round(servo.angle)
        if angle == current:
            return
        if angle > current:
            delta = 1
        else:
            delta = -1

        for i in range(current, angle, delta):
            servo.angle = i
            sleep(rate)

        servo.angle = angle

def gpio_servo(pin = board.D18):
    import pwmio
    pwm = pwmio.PWMOut(pin, duty_cycle=2 ** 15, frequency=50)
    return Servo(pwm, actuation_range=180)

def hat_servo(channel:int = 0):
    from adafruit_pca9685 import PCA9685
    pca = PCA9685(board.I2C())
    pca.frequency = 50
    pwm = pca.channels[channel]
    return Servo(pwm, actuation_range=180)

def crickit_servo(index:int = 0):
    from adafruit_crickit import crickit
    if index == 0:
        return crickit.servo_1
    if index == 1:
        return crickit.servo_2
    if index == 2:
        return crickit.servo_3
    return crickit.servo_4

def run_angles(servo):
    for j in range(5):
        for i in [0,180,90]:
            print(f"Angle = {i}")
            move_servo(servo, i)
            sleep(2)

def sg90(servo:Servo):
    servo.set_pulse_width_range(500,2400)

def mg90s(servo:Servo):
    servo.set_pulse_width_range(500,2500)

