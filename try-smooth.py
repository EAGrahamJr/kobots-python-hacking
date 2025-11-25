import asyncio
from adafruit_crickit import crickit

from pybot.eventbus import EventBus
from pybot.pybot_base import ServoMover, set_mg90s
from edlib import colors as c

# Setup servo
servo1 = set_mg90s(crickit.servo_1)
servo2 = set_mg90s(crickit.servo_3)

sm1 = ServoMover(servo1)
sm2 = ServoMover(servo2)

bus = EventBus()


# Run easing loop
async def sweep_servo1():
    await sm1.smooth(90, 4.0)
    # await asyncio.sleep(10.0)
    await bus.emit("hello", delay_time=1.75)
    await asyncio.sleep(3.0)
    await sm1.soft_landing(0, 4.0)


async def all_done():
    await asyncio.sleep(0.2)
    on_board = crickit.onboard_pixel
    on_board.fill(c.BLACK)
    await asyncio.sleep(0.2)


async def sweep_servo2(delay_time: float):
    # await asyncio.sleep(4.5)
    await sm2.soft_start(180, delay_time)
    await sm2.soft_landing(0, delay_time)


bus.on("hello", sweep_servo2)


# Start event loop
async def run_it():
    # starts running tasks immediately
    # tasks = [asyncio.create_task(sweep_servo1()), asyncio.create_task(sweep_servo2())]
    # can do other stuff
    # await asyncio.gather(*tasks)
    await sweep_servo1()
    await all_done()


asyncio.run(run_it())
