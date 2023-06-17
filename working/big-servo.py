from adafruit_crickit import crickit
from time import sleep
from working.manybuttons import *

ss = crickit.seesaw

# setup buttons and an LED
redButton = Button(REDBUTTON, ss)
yellowButton = Button(YELLOWBUTTON, ss)
greenButton = Button(GREENBUTTON, ss)
redLed = LED(REDLED, ss)
greenLed = LED(GREENLED, ss)
yellowLed = LED(YELLOWLED, ss)
blueLed = LED(BLUELED, ss)

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
