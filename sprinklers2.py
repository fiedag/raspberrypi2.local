import RPi.GPIO as GPIO
import time
import json
import os
import argparse

# datetime calculations
from datetime import datetime

# some safety parameters
MAXRELAYS = 8
MAXTIME=3600 # 1 hour


# get all input paramaters
parser = argparse.ArgumentParser(prog='sprinklers2')
parser.add_argument('-pretend', action='store_true', help='do not actuate the relays, just for testing')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='runtime (in seconds) for the up to $MAXRELAYS RELAYplate relays')
args = parser.parse_args()


relay_map_file = "relay_map_to_gpio_pins.json"
relay_map = {}

# Load existing mapping if available
if not os.path.exists(relay_map_file):
    print("No relay_map_to_gpio_pins.json found. Exiting")
    exit;


with open(relay_map_file, "r") as f:
    relay_map = json.load(f)
print("Loaded existing relay map:")

# Set up the pins needed.  Use BCM pin numbering and set them up as output pins
GPIO.setmode(GPIO.BCM)
for relay, pin in relay_map.items():
    #print(f"relay {relay} is pin {pin}")
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

i=0
for relay, pin in relay_map.items():
    dur = args.integers[i]
    print(f"relay {relay} is pin {pin} and will be on for {dur} seconds")
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(dur)
    GPIO.output(pin, GPIO.LOW)
    i = i + 1

for relay, pin in relay_map.items():
    GPIO.output(pin, GPIO.LOW)


# GPIO.cleanup()





