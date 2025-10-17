#!/usr/bin/env python3
#
# sprinklerstatus.py
#
# Author: Alex Fiedler
# Date: 09-DEC-2020
#
# Interrogates and returns the status of the sprinklers
# The solenoids switch lawn sprinkler circuits 1-5 and dripper circuit 6
#
#

# define the RELAY object
import piplates.RELAYplate as RELAY 


# relaySTATE returns an int from 0 to 127
# the binary of which is the state of the
# relays, e.g.
# 0 = all sprinklers off 
# 0101001 = sprinklers 6,4,1 are on
#
relaystate = RELAY.relaySTATE(0)

def stringout(n,relay):
	if relay==0:
		return ""
	s = ""	
	if (n & 2**(relay-1))!=0:
		s = "Sprinkler {} is on ".format(relay)

	return s + stringout(n, relay-1) 

print(stringout(relaystate,7))
