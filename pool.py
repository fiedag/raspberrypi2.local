#!/usr/bin/env python3
#
# pool.py
#
# Author: Alex Fiedler
# Date: 04-SEP-2021
#
#


# never run anything for >2 hours = 7200 seconds
_MAXTIME=7200

# library for sleeping
import time
# library for processing the input parameters
import argparse

# datetime calculations
from datetime import datetime

# file operations
from pathlib import Path

# get input paramaters
parser = argparse.ArgumentParser(prog='pool')
parser.add_argument('-runpump', required=True, type=int, help='runtime (in seconds) for the poolpump')
parser.add_argument('-gpio', required=True, type=int, help='GPIO Port')
args = parser.parse_args()

# library for General Purpose IO
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

_PUMP_PIN=args.gpio
_PUMP_ON=GPIO.LOW
_PUMP_OFF=GPIO.HIGH

GPIO.setup(_PUMP_PIN, GPIO.OUT)


try:
	t1 = datetime.now()
	GPIO.output(_PUMP_PIN, _PUMP_ON)
	time.sleep(min(args.runpump,_MAXTIME))  # do not leave relay on for more than the max time
	GPIO.output(_PUMP_PIN, _PUMP_OFF)
	t2 = datetime.now()
	msg="Device controlled by pin {} was on for {}".format(_PUMP_PIN, t2 - t1)
	print(msg)
except:
	print("unexpected exception")
	pass
finally:
	GPIO.output(_PUMP_PIN, _PUMP_OFF)

