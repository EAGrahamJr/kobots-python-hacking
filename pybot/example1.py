import asyncio
from adafruit_crickit import crickit

from pybot_base import ServoMover, set_mg90s

# Setup servo
servo1 = set_mg90s(crickit.servo_1)
servo2 = set_mg90s(crickit.servo_3)

sm1 = ServoMover(servo1)
sm2 = ServoMover(servo2)

# Run easing loop
async def sweep_servo1():
    await sm1.smooth(90, 4.0)
    await asyncio.sleep(10.0)
    await sm1.soft_landing(0, 4.0)

async def sweep_servo2():
    await asyncio.sleep(4.5)
    await sm2.soft_start(180, 2.0)
    await sm2.soft_landing(0, 2.0)

# Start event loop
async def run_it():
    # starts running tasks immediately
    tasks = [asyncio.create_task(sweep_servo1()), asyncio.create_task(sweep_servo2())]
    # can do other stuff
    await asyncio.gather(*tasks)

asyncio.run(run_it())
