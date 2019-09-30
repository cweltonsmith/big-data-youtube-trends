#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split('\t')
	chan, views = data
	if len(str(views)) < 20:
		views = str('0' * (20 - len(str(views)))) + str(views)
	print "{0}\t{1}".format(views, chan)
