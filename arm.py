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

_WAIST_HOME = 0

_DEFAULT_RATE = 0.02
_WAIST_RATE = 0.01


class Arm:
    def __init__(self) -> None:
        # Shoulder servo, build 3
        self._shoulder = crickit.servo_3
        self._shoulder.set_pulse_width_range(500, 2400)
        self._shoulder.angle = _SHOULDER_UP
        # Gropper servo, build 3
        self._gripper = crickit.servo_4
        self._gripper.set_pulse_width_range(500, 2400)
        self._gripper.angle = _GRIPPER_CLOSE
        # elbow servo, build 3
        self._elbow = crickit.servo_2
        self._elbow.set_pulse_width_range(500, 2400)
        self._elbow.angle = _ELBOW_STRAIGHT

        # Waist servo, build 3
        self._waist = crickit.servo_1
        self._waist.set_pulse_width_range(500, 2400)
        self._waist.angle = _WAIST_HOME

        self._base = crickit.stepper_motor
        self._base_position = 0.0

    def close(self):
        self.home()

    def home(self):
        self._waist.angle = _WAIST_HOME
        self.gripper = 9
        self.shoulder_park()
        self.elbow_park()

    @property
    def waist(self):
        return self._waist.angle

    @waist.setter
    def waist(self, angle: float, rate: float = _DEFAULT_RATE):
        self._move_servo(self._waist, angle, rate)

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

    def shoulder_park(self, rate=_DEFAULT_RATE):
        self.shoulder(_SHOULDER_UP, rate=rate)

    def elbow_park(self, rate=_DEFAULT_RATE):
        self.elbow(_ELBOW_STRAIGHT, rate=rate)

    @property
    def base(self):
        return self._base_position

    @base.setter
    def base(self, angle: float):
        """Move the base to a certain angle.

        Args:
            angle (float): where to move to
        """
        delta = angle - self._base_position
        steps = 258 * delta/360
        if steps < 0:
            direction = stepper.FORWARD
        else:
            direction = stepper.BACKWARD
        steps = abs(steps)

        for i in range(int(steps)):
            self._base.onestep(direction=direction)
            sleep(_WAIST_RATE)
        self._base_position = angle
        # temporary to keep it from heating up too much
        self._base.release()
