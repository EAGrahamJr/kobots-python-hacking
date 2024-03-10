from adafruit_crickit import crickit
from time import sleep
from edlib import seesaw_util as su

ss = crickit.seesaw

BLUELED = crickit.SIGNAL7
GREENLED = crickit.SIGNAL6
YELLOWLED = crickit.SIGNAL5
REDLED = crickit.SIGNAL4
GREENBUTTON = crickit.SIGNAL3
YELLOWBUTTON = crickit.SIGNAL2
REDBUTTON = crickit.SIGNAL1

# setup buttons and an LED
redButton = su.Button(REDBUTTON, ss)
yellowButton = su.Button(YELLOWBUTTON, ss)
greenButton = su.Button(GREENBUTTON, ss)
redLed = su.LED(REDLED, ss)
greenLed = su.LED(GREENLED, ss)
yellowLed = su.LED(YELLOWLED, ss)
blueLed = su.LED(BLUELED, ss)

servo = crickit.servo_4
servo.set_pulse_width_range(500,2400)
blueIsOn = False

while True:
    sleep(1)
    redValue = redButton.read()
    yellowValue = yellowButton.read()
    greenValue = greenButton.read()

    print(f"Checking {redValue}, {yellowValue}, {greenValue}")

    # used to verify button presses
    if redValue != redLed.value:
        redLed.value = redValue
    if yellowLed.value != yellowValue:
        yellowLed.value = yellowValue
    if greenLed.value != greenValue:
        greenLed.value = greenValue

    if redValue:
        servo.angle = 0
        blueIsOn = True
        blueLed.value = True

    if yellowValue:
        if blueIsOn:
            blueLed.value = False
            blueIsOn = False
        servo.angle = 90

    if greenValue:
        if blueIsOn:
            blueIsOn = False
            servo.angle = 45
        else:
            servo.angle = 180
