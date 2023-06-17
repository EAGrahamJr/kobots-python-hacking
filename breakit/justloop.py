#!/usr/bin/python3

import logging

from adafruit_crickit import crickit
from time import sleep

logging.basicConfig(format='%(asctime)s %(message)s', level=20)
ss = crickit.seesaw

ss.digital_write(crickit.SIGNAL6, ss.INPUT)
ss.digital_write(crickit.SIGNAL7, ss.INPUT)
ss.digital_write(crickit.SIGNAL8, ss.INPUT_PULLDOWN)

motor = crickit.dc_motor_1
servo = crickit.servo_1

padLeft = crickit.touch_1
padRight = crickit.touch_2
padExit = crickit.touch_4

# mini-joystick on 6,7,8 (x,y,z)
def zButton():
    buttonValue = not ss.digital_read(crickit.SIGNAL8)
    #logging.info(f"Press {buttonValue}")
    return buttonValue
def xAxis():
    return ss.analog_read(crickit.SIGNAL6)
def yAxis():
    return ss.analog_read(crickit.SIGNAL7)

lastX = None
lastY = None

try:
    logging.info("Started")

    # run down everything in order
    while True:
        # if padExit.value:
        if zButton():
            logging.info("Done")
            break
        
        # if padLeft.value:
        #     print("padLeft")
            
        # if padRight.value:
        #     print("padRight")
        
        pct = round(xAxis() / 1023.0,2)
        if lastX != pct:
            # print(f"x {pct}")
            servo.angle = 180 * pct
            lastX = pct
        
        pct = round((yAxis() - 512) / 1023.0, 2)
        if lastY != pct:
            # print(f"y {pct}")
            motor.throttle = pct
            lastY = pct

    sleep(1)
    
except KeyboardInterrupt:
    pass
except Exception as Argument:
    logging.exception("Crickit died")
