# PyBot Async Movements

Python motor wrappers to perform async movements, with the aim towards creating "more lifelike" movements. This is simulated throught the use of "easing" functions that change small delays in movements incrementally, to provide a more continuous action.

These are specifically working with the Adafruit CircuitPython `adafruit_motor` classes.

## Base Class

The `BaseMover` provides the basic functional wrappers for the child classes. Each "movement" method returns an `asyncio.Task` with the desired action, which can then be grouped together with others to perform synchronized motions (more-or-less).

* `soft_landing` - gently stop
* `soft_start` - slow start
* `smooth` - ease in and out
* `bounce` - like a bouncing ball
* `linear` - just move

There are a couple of "wrapper" classes specifically for the types of motors:

* `ServoMover` - angular movement by degrees
* `StepperMover` - movement by steps
  * "location" TBD since it can vary by step-style

