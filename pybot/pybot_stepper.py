from adafruit_motor.stepper import StepperMotor
from adafruit_motor import stepper

from .pybot_mover import BaseMover


class StepperMover(BaseMover):
    def __init__(
        self,
        motor: StepperMotor,
        steps_per_rotation: int = 2048,
        delay: float = 0.003,
        step_size: int = stepper.SINGLE,
    ) -> None:
        """
        Async wrapper for a stepper.

        Defaults to the "standard" YP settings of 2048 steps per rotation in single step mode.
        Assumes the "location" of the stepper is 0 at initialization.

        :param motor: the motor
        :param steps_per_rotation: how far it goes (default 2048)
        :param delay: minimum time (seconds) between pulses; useful for "slow" interfaces (default .003 seconds)
        :param style: how to make the motor step (default SINGLE)
        """
        self._motor = motor
        self._speed = delay
        self._style = step_size
        self._current_angle = 0
        self._ratio = 1.0

    @property
    def angle(self) -> float | None:
        return self._current_angle

    async def forward(steps:int, duration: float, easing_fn: Callable[[float], float] = linear):
        return asyncio.create_task(self.move(value, duration, easing_fn))

    def _apply_change(self, value: float) -> None:
        angle = abs(round(value * self._ratio))
        if not angle:
            return

        # TODO angluar change to steps
        steps = angle

        dir = stepper.BACKWARD if value < 0 else stepper.FORWARD

        for i in range(1, steps):
            self._motor.onestep(direction=dir, style=self._style)
            sleep(self._speed)
        self._motor.release()
