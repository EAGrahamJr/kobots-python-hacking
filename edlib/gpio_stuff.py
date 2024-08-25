import pwmio

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
