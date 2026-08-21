from adafruit_motor.stepper import StepperMotor
from adafruit_motor import stepper

from .pybot_base import BaseMover

# TODO NOT READY YET


class StepperMover(BaseMover):
    def __init__(
        self,
        motor: StepperMotor,
        steps_per_rotation: int = 2048,
        delay: float = 0.025,
        step_size: int = stepper.SINGLE,
    ) -> None:
        self._motor = motor
        self._speed = delay
        self._style = step_size
        self._current_angle = 0
        self._ratio = 1.0

    @property
    def angle(self) -> float | None:
        return self._current_angle

    async def soft_landing(self, value: int | float, duration: float) -> Task[None]:
        """
        Gently stop

        :param value: where to
        :param duration: how long (seconds)
        """
        return asyncio.create_task(self.move(value, duration, ease_out_quad))

    async def soft_start(self, value: int | float, duration: float) -> Task[None]:
        """
        Slow start

        :param value: where to
        :param duration: how long (seconds)
        """
        return asyncio.create_task(self.move(value, duration, ease_in_quad))

    def smooth(self, value: int | float, duration: float) -> Task[None]:
        """
        Ease in and out smoothly

        :param value: where to
        :param duration: how long (seconds)
        """
        return asyncio.create_task(self.move(value, duration, ease_in_out_sine))

    def bounce(self, value: int | float, duration: float) -> Task[None]:
        """
        Bouncing ball (best for large moves)

        :param value: where to
        :param duration: how long (seconds)
        """
        return asyncio.create_task(self.move(value, duration, ease_out_bounce))

    async def move():
        pass
