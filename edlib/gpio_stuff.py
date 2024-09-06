import board
import pwmio
import digitalio
from adafruit_motor.servo import Servo

class LED:
    """Dimmable LED """
    def __init__(self, pin) -> None:
        """Create the GPIO LED using PWM

        Args:
            pin (Pin): which GPIO pin
        """
        self._out = pwmio.PWMOut(pin)
        self._out.enabled = True
        self._brightness = 0

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, b):
        if b not in range(101):
            raise ValueError("b must be between 0 and 100")
        self._brightness = b
        self._out.duty_cycle = int((b / 100.0) * 65535)

class Button:
    """Manages a digital pin as a "button" """
    def __init__(self, pin) -> None:
        """Create the button

        Args:
            pin (Pin): which GPIO pin
        """
        self._in = digitalio.DigitalInOut(pin)
        self._in.direction = digitalio.Direction.INPUT
        self._in.pull = digitalio.Pull.UP
        self._pressed = False

    @property
    def value(self) -> bool:
        return not self._in.value

    @property
    def pressed(self) -> bool:
        if self.value and not self._pressed:
            self._pressed = True
        elif not self.value:
            self._pressed = False

def gpio_servo(pin=board.D18) -> Servo:
    """Create a servo for a GPIO pin

    Args:
        pin (Pin, optional): which pin to use. Defaults to board.D18 since it's
        the most common hardware PWM pin

    Returns:
        Servo: an Adafruit "Servo" for the pin
    """
    import pwmio
    pwm = pwmio.PWMOut(pin, duty_cycle=2 ** 15, frequency=50)
    return Servo(pwm, actuation_range=180)
