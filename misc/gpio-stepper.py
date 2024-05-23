# SPDX-FileCopyrightText: 2019 Mikey Sklar for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
import digitalio

coil_A_1_pin = digitalio.DigitalInOut(board.D17)
coil_A_2_pin = digitalio.DigitalInOut(board.D18)
coil_B_1_pin = digitalio.DigitalInOut(board.D10)
coil_B_2_pin = digitalio.DigitalInOut(board.D9)

coil_A_1_pin.direction = digitalio.Direction.OUTPUT
coil_A_2_pin.direction = digitalio.Direction.OUTPUT
coil_B_1_pin.direction = digitalio.Direction.OUTPUT
coil_B_2_pin.direction = digitalio.Direction.OUTPUT

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
    coil_A_1_pin.value = w1
    coil_A_2_pin.value = w2
    coil_B_1_pin.value = w3
    coil_B_2_pin.value = w4

while True:
    user_delay = input("Delay between steps (milliseconds, 0 exits)? ")
    if user_delay is None or user_delay == "" or user_delay == "0":
        break
    user_steps = input("How many steps forward? ")
    forward(int(user_delay) / 1000.0, int(user_steps))
    user_steps = input("How many steps backwards? ")
    backwards(int(user_delay) / 1000.0, int(user_steps))

setStep(0,0,0,0)
