
#!/usr/bin/env python3
#
# sprinklers.py
#
# Author: Alex Fiedler
# Date: 09-DEC-2020
#
# Controls the relay board stacked on raspberrypi.fritz.box
# These relays drive solenoids 1 - 6
# The solenoids switch lawn sprinkler circuits 1-5 and dripper circuit 6
#
#


# define the RELAY object
import piplates.RELAYplate as RELAY 

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
parser = argparse.ArgumentParser(prog='sprinklers')
#parser.add_argument('-every', type=int, choices=[1,2,3,4], default=1, help='run every x days for x = 2..4')
parser.add_argument('-pretend', action='store_true', help='do not actuate the relays, just for testing')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='runtime (in seconds) for the up to seven RELAYplate relays')
args = parser.parse_args()


MAXRELAYS = 7
MAXTIME=3600 # 1 hour

#if not run_this_time(args.every):
	#print("Running every {} days.  Not running today".format(args.every))
	#quit()


import paho.mqtt.client as mqtt #import the client1
#client = mqtt.Client("fiedler.raspberrypi.fritz.box")  # Create instance of client with client ID
#client.connect("broker.mqttdashboard.com", 1883, 60)  # Connect to (broker, port, keepalive-time)


#def publish_mqtt(subtopic, state):
	#client.publish(f'testtopic/melroseave{subtopic}',str(state), 1)


# cycle through the relays
try:
	i = 1
	for x in args.integers:
		if i > MAXRELAYS:
			break
		if x > 0:
			t1 = datetime.now()
			if not args.pretend: RELAY.relayON(0, i)
			#publish_mqtt(f'/sprinkler/{i}',"ON")
			time.sleep(min(x,MAXTIME))  # do not leave relay on for more than the max time
			if not args.pretend: RELAY.relayOFF(0, i)
			#publish_mqtt(f'/sprinkler/{i}','OFF')
			t2 = datetime.now()
			msg="Sprinkler {} was on for {}".format(i, t2 - t1)
			#publish_mqtt("",msg)
			print(msg)
		i += 1
except:
	pass
finally:
	RELAY.relayALL(0, 0)
	time.sleep(5)


