from adafruit_motor.servo import Servo
from .pybot_base import BaseMover


class ServoMover(BaseMover):
    def __init__(self, servo: Servo):
        self._servo = servo

    @property
    def angle(self) -> float | None:
        return self._servo.angle

    def _apply_change(self, value: float) -> None:
        self._servo.angle = round(value)


def set_mg90s(servo: Servo) -> Servo:
    """
    Convenience function that sets the pulse width range and max angle (200) for MG90S (knockoff) servos

    param servo: the servo to set up
    """
    servo.set_pulse_width_range(400, 2600)
    servo.actuation_range = 200
    return servo


def set_sg90(servo: Servo) -> Servo:
    """
    Convenience function that sets the pulse width range and max angle (180) for SG90 (mostly) servos

    param servo: the servo to set up
    """
    servo.set_pulse_width_range(500, 2400)
    servo.actuation_range = 180
    return servo


def set_mg996r(servo: Servo) -> Servo:
    """
    Convenience function that sets the pulse width range and max angle (190) for MG99R6 (knockoff) servos

    param servo: the servo to set up
    """
    servo.set_pulse_width_range(500, 2500)
    servo.actuation_range = 190
    return servo
