import asyncio
import math
from typing import Callable

# Easing curve examples
def linear(t): return t
def ease_in_quad(t): return t * t
def ease_out_quad(t): return t * (2 - t)
def ease_in_out_sine(t): return -(math.cos(math.pi * t) - 1) / 2

async def ease_value(
        start: float,
        end: float,
        duration: float,
        update_fn: Callable[[float], None],
        easing_fn: Callable[[float], float] = linear,
        steps: int = 50
):
    for i in range(steps + 1):
        t = i / steps
        eased_t = easing_fn(t)
        value = start + (end - start) * eased_t
        update_fn(value)
        await asyncio.sleep(duration / steps)
