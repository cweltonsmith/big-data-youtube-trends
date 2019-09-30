#!/usr/bin/python

import sys

#initial values
commentMax = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the channel title, val is the comment amount
#
# The reducer will change the commentMax to the highest comment amount for the channel,
# then the key will change and we'll be dealing with the next channel

#this takes in the data one line at a time
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisComments = data_mapped

    #if a channel is different then the previous channel and max comment amount will be printed
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", commentMax
        oldKey = thisKey;
        commentMax = 0

    #the bit that changes the max value for a channel
    oldKey = thisKey
    if thisComments > commentMax:
	commentMax = thisComments

#prints the last max comment value with the appropriate channel name
if oldKey != None:
    print oldKey, "\t", commentMax
