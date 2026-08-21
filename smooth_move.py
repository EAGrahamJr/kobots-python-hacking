import asyncio
from adafruit_crickit import crickit

from pybot.eventbus import EventBus
from pybot.pybot_servo import ServoMover, set_mg90s, set_mg996r
from edlib import colors as c
from edlib import rotomotor

# Setup servo
sm1 = ServoMover(set_mg996r(crickit.servo_1))
sm2 = ServoMover(set_mg996r(crickit.servo_2))
sm3 = ServoMover(set_mg90s(crickit.servo_3))
sm4 = ServoMover(set_mg90s(crickit.servo_4))

# Setup rotator/turntable
# pivot = rotomotor.RotoStepper(
#     crickit.drive_stepper_motor #, step_size=stepper.INTERLEAVE
# )  # ONCE = 4096
# pivot.speed = 0.005
# pivot.release()


async def pickup():
    d1 = sm1.soft_start(35, 3.0)
    d2 = sm2.soft_landing(90, 5.0)
    d3 = sm3.soft_landing(50, 8.0)
    d4 = sm4.smooth(180, 8.0)
    await asyncio.gather(d1, d2, d3, d4)


async def dropoff():
    await sm4.smooth(90, 2.0)
    pass


async def home():
    d1 = sm1.soft_start(0, 4.0)
    d2 = sm2.soft_start(0, 5.0)
    d3 = sm3.smooth(0, 2.0)
    d4 = sm4.smooth(0, 2.0)
    await asyncio.gather(d1, d3, d2, d4)


async def main():
    await pickup()
    await asyncio.sleep(3.0)
    await dropoff()
    await asyncio.sleep(3.0)
    await home()


asyncio.run(main())
