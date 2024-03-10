#!/usr/bin/python3

import time
from adafruit_crickit import crickit

pp = crickit.drive_1
stopit = crickit.touch_4

pushin = False
while True:
    if stopit.value:
        break
    
    if pushin:
        pp.fraction = 1.0
        pushin = False
    else:
        pp.fraction = 0.0
        pushin = True
    time.sleep(1)

pp.fraction = 0.0