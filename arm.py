from adafruit_crickit import crickit
from adafruit_motor import stepper
from adafruit_motor.stepper import StepperMotor
from time import sleep
from edthings import MG90_RANGE

_SHOULDER_UP = 180
_SHOULDER_DOWN = 120

_ELBOW_UP = 0
_ELBOW_DOWN = 180

_GRIPPER_OPEN = 45
_GRIPPER_CLOSE = 110
_GRIPPER_CLOSE_MOSTLY = 90

_WAIST_HOME = 0

_DEFAULT_RATE = 0.04

class Arm:
    def __init__(self) -> None:
        # Shoulder servo, build 4
        self._shoulder = crickit.servo_1
        MG90_RANGE.apply(self._shoulder)
        self._shoulder.angle = _SHOULDER_UP

        # Gropper servo, build 4
        self._gripper = crickit.servo_3
        MG90_RANGE.apply(self._gripper)
        self._gripper.angle = _GRIPPER_CLOSE

        # elbow servo, build 3
        self._elbow = crickit.servo_2
        MG90_RANGE.apply(self._elbow)
        self._elbow.angle = _ELBOW_DOWN

        # base (e.g. waist) as stepper, build 4
        self._waist = crickit.stepper_motor
        self._waist_position = 0.0

    def close(self):
        self.home()

    def home(self):
        # self.gripper = 9
        self.shoulder = _SHOULDER_UP
        self.elbow = _ELBOW_DOWN
        self.waist = _WAIST_HOME
        self.grpper = _GRIPPER_CLOSE

    @property
    def shoulder(self):
        return self._shoulder.angle

    @shoulder.setter
    def shoulder(self, angle: float, rate: float = _DEFAULT_RATE):
        self._move_servo(self._shoulder, angle, rate)

    @property
    def elbow(self):
        return self._elbow.angle

    @elbow.setter
    def elbow(self, angle: float, rate: float = _DEFAULT_RATE):
        self._move_servo(self._elbow, angle, rate)

    @property
    def gripper(self):
        return self._gripper.angle

    @gripper.setter
    def gripper(self, angle: float, rate: float = 0.001):
        self._move_servo(self._gripper, angle, rate)

    @staticmethod
    def _move_servo(servo, angle: float, rate: float):
        """Move a servo to a certain angle.

        Args:
            servo (Servo): the servo
            angle (float): where to move to
            rate (float): pause between steps in seconds or fractions thereof
        """
        current = int(servo.angle)
        if angle > current:
            delta = 2
        else:
            delta = -2

        for i in range(current, angle, delta):
            servo.angle = i
            sleep(rate)

        servo.angle = angle

    @property
    def waist(self):
        return self._waist_position

    @waist.setter
    def waist(self, angle: float, rate = _DEFAULT_RATE):
        """Move the base to a certain angle.

        Args:
            angle (float): where to move to
        """

        # current gear ratio = 4.67
        delta = angle - self._waist_position
        steps = 200 * 4.67 * delta/360
        if steps < 0:
            direction = stepper.BACKWARD
        else:
            direction = stepper.FORWARD
        steps = abs(steps)

        for i in range(int(steps)):
            self._waist.onestep(direction=direction)
            sleep(rate)
        self._waist_position = angle
        # temporary to keep it from heating up too much
        self._waist.release()
