from time import sleep
from edlib import rotomotor as rm
from adafruit_crickit import crickit
import board
from adafruit_vcnl4040 import VCNL4040

##############################################################################
# An interesting way to see what the proximity sensor does when presented with
# a "controlled" target
##############################################################################
rotor = rm.RotoStepper(crickit.drive_stepper_motor)
rotor.release()

i2c = board.I2C()
sensor = VCNL4040(i2c)

def reset():
    print(f"Sensor start {sensor.proximity}")
    while sensor.proximity < 90:
        rotor.backward(2)
    print(f"Sensor end {sensor.proximity}")

# LED duty changes
cycles = (VCNL4040.LED_1_40, VCNL4040.LED_1_80, VCNL4040.LED_1_160, VCNL4040.LED_1_320)
current_cycle = sensor.led_duty_cycle
print(f"Current cycle: {cycles.index(current_cycle)}")

# for c in cycles:
#     print(f"Setting to {c}")
#     sensor.led_duty_cycle = c
#     rotor.forward(200)
#     reset()
#     sleep(1)

# sensor.led_duty_cycle = current_cycle

currents = (VCNL4040.LED_50MA, VCNL4040.LED_75MA, VCNL4040.LED_100MA, VCNL4040.LED_120MA, VCNL4040.LED_140MA, VCNL4040.LED_160MA, VCNL4040.LED_180MA, VCNL4040.LED_200MA)
current_led = sensor.led_current
print(f"Current current {current_led}")

for c in currents:
    print(f"Setting LED current to {c}")
    sensor.led_current = c
    rotor.forward(200)
    reset()
    sleep(1)

sensor.led_current = current_led
