import RPi.GPIO as GPIO
import time
import json
import os
import argparse

# datetime calculations
from datetime import datetime

# some safety parameters
MAXTIME=3600 # 1 hour
MINTIME=5 # 5 seconds min watering time



def parse_pair(string):
    try:
        x, y = string.split(',')
        return (float(x), float(y))
    except ValueError:
        raise argparse.ArgumentTypeError(f"tuples must be x,y format")

parser = argparse.ArgumentParser()

# seven watering sectors.  the eigth is the fertiliser
for i in range(1,8):
    parser.add_argument(f'-r{i}', type=parse_pair,
                    help=f'Tuple r{i} (e.g. 1,2)')

parser.add_argument('-test', action='store_true',
                    help='Run in test mode (no GPIO operations)')

parser.add_argument('-off', action='store_true',
                    help='Turn off all relays immediately')


args = parser.parse_args()

GPIO_HIGH = GPIO.HIGH
# Use the test flag
if args.test:
    print("Running in TEST mode - GPIO operations will be simulated")
    GPIO_HIGH = GPIO.LOW


supplied_relays = []
for i in range(1, 8):
    param_value = getattr(args, f'r{i}')
    if param_value is not None:
        supplied_relays.append((i, param_value))


relay_map_file = "/home/pi/relay_map_to_gpio_pins.json"
relay_map = {}

# Load existing mapping if available
if not os.path.exists(relay_map_file):
    print("No relay_map_to_gpio_pins.json found. Exiting")
    exit;


with open(relay_map_file, "r") as f:
    relay_map = json.load(f)
# print("Loaded existing relay map:")

# Set up the pins needed.  Use BCM pin numbering and set them up as output pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for relay, pin in relay_map.items():
    #print(f"relay {relay} is pin {pin}")
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
if args.off:
    # above initialisation already turned everything off.  no more to do.
    print("All relays turned off. Exiting.")
    exit(0);


fert_pin = relay_map["8"]

# Display what was supplied
print(f"Supplied {len(supplied_relays)} relay configurations:")
for position, (relay_num, (water, fert)) in enumerate(supplied_relays, start=1):
    water_pin = relay_map[str(relay_num)]

    print(f"  Position {position}: Relay {relay_num} (Pin {water_pin}) -> water={water:.1f}, fert={fert:.1f}")
    # turn water on for initial MINTIME seconds
    print(f"                       Relay {relay_num} initially on for {MINTIME} seconds")
    GPIO.output(water_pin, GPIO_HIGH)
    time.sleep(MINTIME)

    fert_duration = 0
    if fert > 0:
        fert_duration = max(fert, MINTIME)
        print(f"                       Fertiliser on for {fert_duration} seconds")
        GPIO.output(fert_pin, GPIO_HIGH)
        time.sleep(fert_duration)
        print(f"                       Fertiliser off again")
        GPIO.output(fert_pin, GPIO.LOW)
    
    water_duration_remaining = water - fert_duration - MINTIME
    print(f"                       Water remains on for another {water_duration_remaining} seconds")
    # wait another water - fert - MINTIME seconds
    time.sleep( water_duration_remaining )
    GPIO.output(water_pin, GPIO.LOW)
    
