# SPDX-FileCopyrightText: 2019 Mikey Sklar for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
import digitalio
from adafruit_motor.stepper import StepperMotor
from adafruit_motor import stepper

pinA1 = digitalio.DigitalInOut(board.D17)
pinA2 = digitalio.DigitalInOut(board.D18)
pinB1 = digitalio.DigitalInOut(board.D10)
pinB2 = digitalio.DigitalInOut(board.D9)

pinA1.direction = digitalio.Direction.OUTPUT
pinA2.direction = digitalio.Direction.OUTPUT
pinB1.direction = digitalio.Direction.OUTPUT
pinB2.direction = digitalio.Direction.OUTPUT

def forward(delay, steps):
    i = 0
    while i in range(0, steps):
        # setStep(1, 0, 1, 0)
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        # setStep(0, 1, 1, 0)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        # setStep(0, 1, 0, 1)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        # setStep(1, 0, 0, 1)
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        i += 1

def backwards(delay, steps):
    i = 0
    while i in range(0, steps):
        # setStep(1, 0, 0, 1)
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        # setStep(0, 1, 0, 1)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        # setStep(0, 1, 1, 0)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        # setStep(1, 0, 1, 0)
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        i += 1

def setStep(w1, w2, w3, w4):
    pinA1.value = w1
    pinA2.value = w2
    pinB1.value = w3
    pinB2.value = w4

def oldschool():
    user_delay = input("Delay between steps (milliseconds, 0 exits)? ")
    if user_delay is None or user_delay == "" or user_delay == "0":
        setStep(0,0,0,0)
        return False
    user_steps = input("How many steps forward? ")
    forward(int(user_delay) / 1000.0, int(user_steps))
    user_steps = input("How many steps backwards? ")
    backwards(int(user_delay) / 1000.0, int(user_steps))
    return True

def newschool():
    st = StepperMotor(pinA1,pinB1,pinA2,pinB2,microsteps=None)
    user_delay = input("Delay between steps (milliseconds, 0 exits)? ")
    if user_delay is None or user_delay == "" or user_delay == "0":
        st.release()
        return False
    delay = float(user_delay) / 1000.0

    steps = int(input("How many steps forward? "))
    i = 0
    while i in range(0, steps):
        st.onestep(direction = stepper.FORWARD, style = stepper.INTERLEAVE)
        time.sleep(delay)
        i += 1

    steps = int(input("How many steps backwards? "))
    i = 0
    while i in range(0, steps):
        st.onestep(direction = stepper.BACKWARD, style = stepper.INTERLEAVE)
        time.sleep(delay)
        i += 1

    return True

b = True
while b:
    # b = oldschool()
    b = newschool()

