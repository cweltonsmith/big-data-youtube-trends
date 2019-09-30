#!/usr/bin/python
#Format of each line is:
#channel_title, dislikes

import sys

disTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip("\t") #strip the tab
    if len(data_mapped) != 2:
        # Something has gone worng. Skip this line.
        continue

    thisKey, thisValue = data_mapped #sets the value pair

    #Inital state
    if oldKey and oldKey != thisKey:
        print oldkey, ",", disTotal
        oldKey = thisKey;
        disTotal = 0
    #setting keys and adding total dislikes per channel video
    oldKey = thisKey
    disTotal += float(thisValue)

if oldKey !=None:
    print oldKey, ",", disTotal