import asyncio
from adafruit_crickit import crickit

from easefunc import ease_value, ease_in_out_sine, ease_out_quad

# Setup servo
servo = crickit.servo_1

servo.set_pulse_width_range(400,2600)
servo.actuation_range = 200

# Async wrapper for servo update
def set_servo_angle(angle):
    servo.angle = angle

# Run easing loop
async def sweep_servo():
    await ease_value(0, 90, duration=2.0, update_fn=set_servo_angle, easing_fn=ease_in_out_sine, steps=100)
    await ease_value(90, 0, duration=2.0, update_fn=set_servo_angle, easing_fn=ease_out_quad, steps=100)

# Start event loop
asyncio.run(sweep_servo())
