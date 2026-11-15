from abc import ABC, abstractmethod
import asyncio
from typing import Callable

from .easefunc import (
    ease_in_out_sine,
    ease_in_quad,
    ease_out_bounce,
    ease_out_quad,
    linear,
)


class BaseMover(ABC):
    @property
    @abstractmethod
    def angle(self) -> float | None:
        pass

    @abstractmethod
    def _apply_change(self, value: float) -> None:
        pass

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

    async def move(
        self,
        requested: int | float,
        duration: float,
        easing_fn: Callable[[float], float] = linear,
    ):
        """
        Move the device to mumble angle.

        :param value: where to
        :param duration: how long (seconds)
        :param easing_fn: how to get there; default is linear (e.g. no acceleration)
        """
        start = self.angle if self.angle is not None else 0
        diff = requested - start
        steps = abs(int(diff))

        if not steps:
            return

        for i in range(steps + 1):
            t = i / steps
            eased_t = easing_fn(t)
            value = start + diff * eased_t
            self._apply_change(value)
            await asyncio.sleep(duration / steps)
