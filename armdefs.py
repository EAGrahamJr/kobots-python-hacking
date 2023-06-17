from adafruit_crickit import crickit
from adafruit_motor import stepper
from adafruit_motor.stepper import StepperMotor
from time import sleep

_SHOULDER_UP = 180
_SHOULDER_DOWN = 20

_ELBOW_STRAIGHT = 0
_ELBOW_BENT = 90

_GRIPPER_OPEN = 60
_GRIPPER_CLOSE = 9
_GRIPPER_CLOSE_MOSTLY = 15

_STEPPER_STEPS = 200 * 1.32

_DEFAULT_RATE = .05

class Arm:
    def __init__(self) -> None:
        # Shoulder servo, build 2
        self.shoulder = crickit.servo_3
        self.shoulder.set_pulse_width_range(500,2400)
        self.shoulder.angle = _SHOULDER_UP
        # Gropper servo, build 2
        self.gripper = crickit.servo_4
        self.gripper.set_pulse_width_range(500,2400)
        self.gripper.angle = _GRIPPER_CLOSE
        # elbow servo, build 2
        self.elbow = crickit.servo_2
        self.elbow.set_pulse_width_range(500,2400)
        self.elbow.angle = _ELBOW_STRAIGHT

        # Waist stepper
        self.waist = crickit.stepper_motor
        self.waist.release()

    def close(self):
        self.home()

    def home(self):
        self.waist.release()
        self.gripper_close()
        self.shoulder_park()
        self.elbow_park()

    def shoulder_move(self,angle,rate=_DEFAULT_RATE):
        self._move_servo(self.shoulder, angle, rate)

    def elbow_move(self,angle,rate=_DEFAULT_RATE):
        self._move_servo(self.elbow, angle, rate)

    def gripper_move(self, angle, rate=.001):
        self._move_servo(self.gripper, angle, rate)

    @staticmethod
    def _move_servo(servo, angle, rate):
        current = int(servo.angle)
        if angle > current:
            delta = 2
        else:
            delta = -2

        for i in range(current, angle, delta):
            servo.angle = i
            sleep(rate)

        servo.angle = angle

    def shoulder_park(self,rate=_DEFAULT_RATE):
        # home
        self.shoulder_move(_SHOULDER_UP, rate=rate)

    def elbow_park(self, rate=_DEFAULT_RATE):
        self.elbow_move(_ELBOW_STRAIGHT, rate=rate)

    def waist_move(self,steps:int,forward=True,rate=.02):
        if forward:
            which_way = stepper.BACKWARD
        else:
            which_way = stepper.FORWARD

        for i in range(steps):
            self.waist.onestep(direction=which_way)
            sleep(rate)
        self.waist.release()

    def gripper_greedy(self, ignored, pause, rate):
        for i in range(4):
            self.gripper_open()
            sleep(rate)
            self.gripper_close()
            sleep(rate)
        sleep(pause)

    def gripper_open(self):
        self.gripper.angle = _GRIPPER_OPEN

    def gripper_close(self):
        self.gripper.angle = _GRIPPER_CLOSE