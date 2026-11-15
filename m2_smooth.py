from edlib import rotoservo as rs
#import adafruit_vl6180x
import board
import asyncio

from pybot.pybot_servo import ServoMover, set_mg90s
from adafruit_motor.servo import Servo

from adafruit_pca9685 import PCA9685

pca = PCA9685(board.I2C())
pca.frequency = 50


def hat(channel) -> Servo:
    pwm = pca.channels[channel]
    return Servo(pwm, actuation_range=180)

sx = []
for i in range(0,7):
    servo = set_mg90s(hat(i))
    sm = ServoMover(servo)
    sx.append(sm)

async def up(offset:int)->None:
    await asyncio.sleep((len(sx) - 1 - offset) * .05)
    await sx[offset].soft_landing(value=90, duration=2.0)

async def down(offset:int) -> None:
    await asyncio.sleep(offset * .25)
    await sx[offset].soft_start(value=0, duration=2.0)

async def main()->None:
    await asyncio.gather(*(up(i) for i in range(len(sx))))
    await asyncio.sleep(2.0)
    await asyncio.gather(*(down(i) for i in range(len(sx))))

if __name__ == "__main__":
    asyncio.run(main())
