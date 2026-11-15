
import asyncio

from adafruit_crickit import crickit

from easefunc import ease_in_out_sine, ease_in_quad, ease_out_quad

from metaphor import Cue, DemoServo, Movement, Scene, play_scene, run_cues

# servo1 = DemoServo("servo1")
# servo2 = DemoServo("servo2")

servo1 = crickit.servo_1
servo2 = crickit.servo_2

scene1 = Scene(
    name="Curtain Rise",
    duration=2.0,
    movements=[
        Movement(servo1, 0, 90, ease_in_quad),
        Movement(servo2, 180, 90, ease_out_quad)
    ]
)

scene2 = Scene(
    name="Spotlight Sweep",
    duration=3.0,
    movements=[
        Movement(servo1, 90, 0, ease_in_out_sine),
        Movement(servo2, 90, 180, ease_in_out_sine)
    ]
)


async def perform():
    await play_scene(scene1)
    await asyncio.sleep(0.5)  # dramatic pause
    await play_scene(scene2)


scene3 = Scene(
    name="Bow",
    duration=1.5,
    movements=[
        Movement(servo1, 0, 45, ease_in_out_sine),
        Movement(servo2, 180, 135, ease_in_out_sine)
    ]
)

cue_sheet = [
    Cue(trigger_time=0.0, next_scene=scene1),
    Cue(trigger_time=2.5, next_scene=scene2),
    Cue(trigger_time=6.0, next_scene=scene3),
]


async def cued_performance():
    await run_cues(cue_sheet)


if __name__ == "__main__":
    asyncio.run(perform())
    asyncio.run(cued_performance())
