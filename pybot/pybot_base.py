from abc import ABC, abstractmethod
import asyncio
from typing import Callable
from adafruit_motor.servo import Servo

from pybot.easefunc import ease_in_out_sine, ease_in_quad, ease_out_quad, linear

class BaseMover(ABC):
    @property
    @abstractmethod
    def angle(self) -> float|None:
        pass
    @angle.setter
    @abstractmethod
    def angle(self, value:float) -> None:
        pass

    @abstractmethod
    def _apply_move(self, value:float) -> None:
        pass

    async def soft_landing(self, value:int|float, duration:float, steps:int = 200):
        await self.move(value, duration, steps, ease_out_quad)

    async def soft_start(self, value:int|float, duration:float, steps:int = 200):
        await self.move(value, duration, steps, ease_in_quad)

    async def smooth(self, value:int|float, duration:float, steps:int = 200):
        await self.move(value,duration,steps,ease_in_out_sine)

    async def move(self, end:int|float, duration:float, steps:int = 200, easing_fn:Callable[[float], float] = linear):
        start = self.angle if self.angle is not None else 0
        diff = (end - start)

        for i in range(steps + 1):
            t = i / steps
            eased_t = easing_fn(t)
            value = start + diff * eased_t
            self._apply_move(value)
            await asyncio.sleep(duration / steps)

class ServoMover(BaseMover):
    def __init__(self, servo:Servo):
        self._servo = servo
        # TODO do we set the intial angle here?

    @property
    def angle(self) -> float|None:
        return self._servo.angle

    @angle.setter
    def angle(self, value:float) -> None:
        asyncio.create_task(self.soft_landing(value, 1.0))

    def _apply_move(self, value: float) -> None:
        self._servo.angle = round(value)

def set_mg90s(servo:Servo)->Servo:
    """
    Convenience function that sets the pulse width range and max angle (200) for MG90S servos

    param servo: the servo to set up
    """
    servo.set_pulse_width_range(400,2600)
    servo.actuation_range = 200
    return servo

def set_sg90(servo:Servo)->Servo:
    """
    Convenience function that sets the pulse width range and max angle (180) for SG90 servos

    param servo: the servo to set up
    """
    servo.set_pulse_width_range(500,2400)
    servo.actuation_range = 180
    return servo
