from adafruit_motor.stepper import StepperMotor
from adafruit_motor import stepper
from time import sleep

class RotoStepper:
    def __init__(self, motor:StepperMotor, delay:float=.001, step_size:int = stepper.SINGLE) -> None:
        self.motor = motor
        self.delay = delay
        self.style = step_size

    def forward(self,steps:int):
        self.__run(steps)

    def backward(self,steps:int):
        self.__run(steps, dir=stepper.BACKWARD)

    def release(self):
        self.motor.release()

    def __run(self,steps:int, dir:int = stepper.FORWARD):
        for i in range(1,steps):
            self.motor.onestep(direction=dir, style=self.style)
            sleep(self.delay)
        self.motor.release()

