
from adafruit_motor.servo import Servo

class ServoRange:
    def __init__(self, lower=900, upper=2400):
        self._lower = lower
        self._upper = upper

    @property
    def lower(self):
        return self._lower

    @property
    def upper(self):
        return self._upper

    def apply(self, servo: Servo):
        servo.set_pulse_width_range(self._lower, self._upper)


MG90_RANGE = ServoRange(500,2400)