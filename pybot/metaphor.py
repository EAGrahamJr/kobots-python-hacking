import asyncio

from easefunc import ease_in_out_sine, ease_in_quad, ease_out_quad, ease_value


class Scene:
    """A named block of choreography: a set of Movements that all run together for `duration`."""

    def __init__(self, name, duration, movements):
        self.name = name
        self.duration = duration  # in seconds
        self.movements = movements  # list of Movement objects


class Movement:
    """One servo's part within a Scene: ease from start_angle to end_angle over the Scene's duration."""

    def __init__(self, servo, start_angle, end_angle, easing_fn):
        self.servo = servo
        self.start_angle = start_angle
        self.end_angle = end_angle
        self.easing_fn = easing_fn


class Cue:
    """A scheduled trigger: play next_scene once trigger_time (seconds since the cue sheet started) is reached."""

    def __init__(self, trigger_time, next_scene):
        self.trigger_time = trigger_time
        self.next_scene = next_scene


class DemoServo:
    """Minimal stand-in for adafruit_motor.servo.Servo so this file runs without hardware attached."""

    def __init__(self, label):
        self.label = label
        self.angle = 0

    def __repr__(self):
        return f"<DemoServo {self.label} angle={self.angle:.1f}>"


async def play_scene(scene: Scene) -> None:
    """Run every Movement in a Scene concurrently, so they all finish together after scene.duration."""
    print(f"🎭 Scene: {scene.name}")

    def make_update_fn(servo):
        return lambda angle: setattr(servo, 'angle', angle)

    tasks = [
        ease_value(
            move.start_angle,
            move.end_angle,
            scene.duration,
            make_update_fn(move.servo),
            move.easing_fn,
        )
        for move in scene.movements
    ]
    await asyncio.gather(*tasks)


async def run_cues(cues: list[Cue]) -> None:
    """Play a cue sheet: each Cue's Scene starts at its trigger_time, measured from when run_cues began."""
    start = asyncio.get_event_loop().time()
    for cue in cues:
        elapsed = asyncio.get_event_loop().time() - start
        wait = cue.trigger_time - elapsed
        if wait > 0:
            await asyncio.sleep(wait)
        await play_scene(cue.next_scene)

