import pwmio
import digitalio

class LED:
    def __init__(self, pin) -> None:
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
    def __init__(self, pin) -> None:
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
