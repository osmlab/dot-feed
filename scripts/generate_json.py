#!/usr/bin/env python3

import simplejson as json
import csv

dots = {}

with open('state_table.csv', 'r') as states_in:
	states = csv.reader(states_in)
	for state in states:
		dots[state[0]] = {
			"website": state[2],
			"twitter": "",
			"rss": ""
		}

with open('dot-feed.json', 'w') as fhandle:
	json.dump(dots, fhandle, sort_keys=True, indent='    ')
