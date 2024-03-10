from adafruit_seesaw.seesaw import Seesaw

class Button:
    def __init__(self,signal:int,see_saw:Seesaw):
        self._signal = signal
        self._ss = see_saw
        self._ss.digital_write(signal, self._ss.INPUT_PULLUP)

    def read(self)->None:
        return not self._ss.digital_read(self._signal)

class LED:
    def __init__(self,signal:int,see_saw:Seesaw):
        self._signal = signal
        self._ss = see_saw
        self._ss.digital_write(signal, self._ss.OUTPUT)
        self._value = False
        self._ss.digital_write(self._signal, False)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, b):
        print(f"LED is {b}")
        self._ss.digital_write(self._signal, b)
        self._value = b
