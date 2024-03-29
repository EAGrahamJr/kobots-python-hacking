#!/bin/env python3

# !/usr/bin/env python
# ----------------------------------------------------------------------
# qwiic_alphanumeric_ex3_print_char.py
#
# This example tests illuminating a whole character on the 14-segment display.
# ----------------------------------------------------------------------
#
# Written by Priyanka Makin @ SparkFun Electronics, September 2021
#
# This python library supports the SparkFun Electronics qwiic sensor/
# board ecosystem on a Raspberry Pi (and compatable) single board
# computers.
#
# More information on qwiic is at https://www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun by buying a board!
#
# ======================================================================
# Copyright (c) 2021 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#=======================================================================
# Example 3

from __future__ import print_function
import qwiic_alphanumeric
# import time
import sys

def run_example():

    print("\nSparkFun Qwiic Alphanumeric - Example 3: Print Char")
    my_display = qwiic_alphanumeric.QwiicAlphanumeric()

    if my_display.begin() == False:
        print("\nThe Qwiic Alphanumeric isn't connected to the system. Please check your connection.", \
            file=sys.stderr)
        return

    print("\nQwiic Alphanumeric ready!")

    print("Changing address")
    # my_display.set_i2c_address(0x6F)

    # my_display.set_brightness(12)
    # my_display.print("A")
    # my_display.print_char('A',1)
    # my_display.decimal_on = True
    # my_display.colon_on = True
    my_display.print("YO!")
    my_display.update_display()

    # # Un comment these lines if you want to see all available characters
    # # Print to every digit of a given display
    # for digit_num in range(0, 4):
    #     for i in range(ord(' '), ord('~')):
    #         if i is not ord(':') or ord('.'):
    #             my_display.print_char(chr(i), digit_num)
    #             my_display.update_display()
    #             time.sleep(1)
    #             my_display.clear()
    input()
    my_display.clear()

if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 3")
        sys.exit(0)
