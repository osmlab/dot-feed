#!/usr/bin/env python3

import simplejson as json

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "DC"]

dots = {}

for state in states:
	dots[state] = {
		"website": "",
		"twitter": "",
		"rss": ""
	}

with open('dot-feed.json', 'w') as fhandle:
	json.dump(dots, fhandle, sort_keys=True, indent='    ')
