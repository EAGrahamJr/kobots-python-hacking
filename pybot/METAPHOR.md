# `metaphor.py`

A tiny choreography engine for running multiple servos through eased, timed
motions in concert — think "stage directions" for a robot. It's independent
of the `BaseMover`/`ServoMover` abstraction in [`pybot_mover.py`](pybot_mover.py)
and [`pybot_servo.py`](pybot_servo.py); instead it drives any object with a
settable `.angle` attribute directly via [`ease_value`](easefunc.py), which is
why the demo below uses a lightweight `DemoServo` stand-in rather than a real
`adafruit_motor.servo.Servo`.

## Classes and how they relate

```
Cue ──points to──> Scene ──contains──> [Movement, Movement, ...]
                                              │
                                              └─ acts on a servo (e.g. DemoServo,
                                                 or a real adafruit Servo)
```

- **`Movement`** — the smallest unit: one servo's journey from `start_angle`
  to `end_angle`, using a given `easing_fn` (from [`easefunc.py`](easefunc.py),
  e.g. `ease_in_quad`, `ease_out_quad`, `ease_in_out_sine`). A `Movement`
  doesn't know how long it takes — that's the `Scene`'s job.

- **`Scene`** — a named group of `Movement`s that all play out over the same
  `duration`. Every `Movement` in a `Scene` starts at the same time and
  finishes at the same time, so a `Scene` is how you keep several servos in
  sync (e.g. two "curtain" servos closing together).

- **`Cue`** — pairs a `trigger_time` with the `Scene` that should play next.
  It models a scheduled scene transition (e.g. "at t=10s, cut to Scene 2").
  A list of `Cue`s forms a cue sheet, played back by `run_cues`.

- **`DemoServo`** — not part of the choreography model; it's just a stand-in
  object with a plain `.angle` attribute so `metaphor.py` can run standalone
  without hardware. Swap in a real `adafruit_motor.servo.Servo` (see
  [`pybot_servo.py`](pybot_servo.py) for setup helpers like `set_sg90`) to
  drive actual servos.

## `play_scene(scene)`

```python
async def play_scene(scene: Scene) -> None:
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
```

For each `Movement` in the `Scene`, `play_scene` builds an `ease_value(...)`
coroutine (from `easefunc.py`) that steps the movement's servo from
`start_angle` to `end_angle` over `scene.duration`, shaped by that movement's
`easing_fn`. `make_update_fn(servo)` closes over the *specific* servo for
that movement so each coroutine updates the right one — this avoids the
classic Python closure bug where a `lambda` defined in a loop captures the
loop variable by reference instead of by value.

All of a scene's movements are collected into `tasks` *before* awaiting, then
run together with a single `asyncio.gather(*tasks)`. That's what makes them
concurrent.

## `run_cues(cues)`

```python
async def run_cues(cues: list[Cue]) -> None:
    start = asyncio.get_event_loop().time()
    for cue in cues:
        elapsed = asyncio.get_event_loop().time() - start
        wait = cue.trigger_time - elapsed
        if wait > 0:
            await asyncio.sleep(wait)
        await play_scene(cue.next_scene)
```

`run_cues` plays a cue sheet — a list of `Cue`s — against a shared clock that
starts ticking the moment `run_cues` is called. For each `Cue`, in order, it
works out how much longer to wait until that cue's `trigger_time` has
elapsed, sleeps that long (or not at all, if the previous scene already ran
past it), then plays `cue.next_scene`. Unlike `perform()`'s hardcoded
sequence of `await play_scene(...)` calls, `trigger_time` is measured from
the *start of the cue sheet*, not from the end of the previous scene — so
cues can be spaced out independent of how long each scene actually takes
(as long as scenes don't run long enough to make a later cue's wait go
negative, in which case that scene just starts immediately instead of on
time).

## Example (from `perform()`)

```python
scene1 = Scene(
    name="Curtain Rise",
    duration=2.0,
    movements=[
        Movement(servo1, 0, 90, ease_in_quad),
        Movement(servo2, 180, 90, ease_out_quad),
    ],
)

scene2 = Scene(
    name="Spotlight Sweep",
    duration=3.0,
    movements=[
        Movement(servo1, 90, 0, ease_in_out_sine),
        Movement(servo2, 90, 180, ease_in_out_sine),
    ],
)


async def perform():
    await play_scene(scene1)
    await asyncio.sleep(0.5)  # dramatic pause
    await play_scene(scene2)


if __name__ == "__main__":
    asyncio.run(perform())
```

Running `perform()`:

1. Plays `scene1` ("Curtain Rise") — `servo1` eases in-quad from 0°→90°
   while `servo2` eases out-quad from 180°→90°, both finishing after 2s.
2. Waits 0.5s.
3. Plays `scene2` ("Spotlight Sweep") — `servo1` and `servo2` sine-ease to
   swapped positions (90°→0° and 90°→180°), both finishing after 3s.

## Example (cue sheet, via `run_cues`)

```python
scene3 = Scene(
    name="Bow",
    duration=1.5,
    movements=[
        Movement(servo1, 0, 45, ease_in_out_sine),
        Movement(servo2, 180, 135, ease_in_out_sine),
    ],
)

cue_sheet = [
    Cue(trigger_time=0.0, next_scene=scene1),
    Cue(trigger_time=2.5, next_scene=scene2),
    Cue(trigger_time=6.0, next_scene=scene3),
]


async def cued_performance():
    await run_cues(cue_sheet)
```

This is the same "curtain rise, then spotlight sweep" performance as
`perform()`, plus a closing `scene3` ("Bow"), but driven by a cue sheet
instead of hardcoded `await`s:

1. `t=0.0s` — `scene1` ("Curtain Rise") starts, runs 2s.
2. `t=2.5s` — `scene2` ("Spotlight Sweep") starts (a 0.5s gap after
   `scene1` ends, same as `perform()`'s dramatic pause), runs 3s, ending
   at `t=5.5s`.
3. `t=6.0s` — `scene3` ("Bow") starts (another 0.5s gap) and runs 1.5s.

Run either demo directly with:

```bash
uv run python -m pybot.metaphor
```

which runs `perform()` followed by `cued_performance()`.
