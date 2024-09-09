from adafruit_motor.stepper import StepperMotor
from adafruit_motor import stepper
from time import sleep
from digitalio import DigitalInOut,Direction

class RotoStepper:
    def __init__(self, motor:StepperMotor, delay:float=.025, step_size:int = stepper.SINGLE) -> None:
        self._motor = motor
        self._speed = delay
        self._style = step_size
        self._ratio = 1.0

    @property
    def speed(self)->float:
        """The amount of "time" to sleep between steps (defaults to .025)

        Returns:
            float: pause time
        """
        return self._speed

    @speed.setter
    def speed(self, howFast:float=0.025):
        """Sets the "speed"

        Args:
            howFast (float, optional): the speed to use. Defaults to 0.025.
        """
        self._speed = howFast

    @property
    def gear_ratio(self):
        return self._ratio
    @gear_ratio.setter
    def gear_ratio(self, f:float):
        self._ratio = f

    def forward(self,steps:int):
        self.__run(steps)

    def backward(self,steps:int):
        self.__run(steps, dir=stepper.BACKWARD)

    def release(self):
        self._motor.release()

    def __run(self,steps:int, dir:int = stepper.FORWARD):
        actual = round(steps * self._ratio)
        for i in range(1,actual):
            self._motor.onestep(direction=dir, style=self._style)
            sleep(self._speed)
        self._motor.release()

def digitalStepper(pinA1,pinA2,pinB1,pinB2) -> RotoStepper:
    """
    A1, A2, B1, B2
    """
    pA1 = DigitalInOut(pinA1)
    pA1.direction = Direction.OUTPUT
    pA2 = DigitalInOut(pinA2)
    pA2.direction = Direction.OUTPUT
    pB1 = DigitalInOut(pinB1)
    pB1.direction = Direction.OUTPUT
    pB2 = DigitalInOut(pinB2)
    pB2.direction = Direction.OUTPUT
    step1 = StepperMotor(pA1,pB1,pA2,pB2, microsteps=None)
    return RotoStepper(step1, step_size=stepper.INTERLEAVE)
