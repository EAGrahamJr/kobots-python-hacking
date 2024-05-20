from adafruit_motor.stepper import StepperMotor
from adafruit_motor import stepper
from time import sleep

class RotoStepper:
    def __init__(self, motor:StepperMotor, delay:float=.001, step_size:int = stepper.SINGLE) -> None:
        self._motor = motor
        self._speed = delay
        self._style = step_size

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

    def forward(self,steps:int):
        self.__run(steps)

    def backward(self,steps:int):
        self.__run(steps, dir=stepper.BACKWARD)

    def release(self):
        self._motor.release()

    def __run(self,steps:int, dir:int = stepper.FORWARD):
        for i in range(1,steps):
            self._motor.onestep(direction=dir, style=self._style)
            sleep(self._speed)
        self._motor.release()

