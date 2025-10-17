#!/usr/bin/env python3
#
# gpio_test.py
#
# Author: Alex Fiedler
# Date: 18-FEB-2025
#
# Controls the relay board stacked on raspberrypi.fritz.box
# These relays drive solenoids 1 - 6
# The solenoids switch lawn sprinkler circuits 1-5 and dripper circuit 6
#
#

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

# library for sleeping
import time
# library for processing the input parameters
import argparse

# datetime calculations
from datetime import datetime

# file operations
from pathlib import Path

# a way to skip days
from skipper import run_this_time

# get all input paramaters
#parser = argparse.ArgumentParser(prog='sprinklers')
#parser.add_argument('-every', type=int, choices=[1,2,3,4], default=1, help='run every x days for x = 2..4')
#parser.add_argument('-pretend', action='store_true', help='do not actuate the relays, just for testing')
#parser.add_argument('integers', metavar='N', type=int, nargs='+', help='runtime (in seconds) for the up to seven RELAYplate relays')
#args = parser.parse_args()


MAXRELAYS = 7
MAXTIME=3600 

GPIO.output(7,GPIO.HIGH)
time.sleep(5)
GPIO.output(7,GPIO.LOW)

