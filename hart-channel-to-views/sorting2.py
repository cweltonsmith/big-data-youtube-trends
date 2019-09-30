#!/usr/bin/python

import sys

counter = 0
for line in sys.stdin:
	if counter != 10:
		data = line.strip().split('\t')
		views, chan = data
		i = 0
		while (str(views)[i] == '0'):
			i += 1
		views = str(views)[i:]
		print views, '\t', chan
		counter += 1
	else:
		break
