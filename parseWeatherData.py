#!/usr/bin/env python3

# Parse data collected from sensors, display
# with matplotlib or something.
# Doesn't work if you don't have any data.
# Maybe convert to jupyter notebook at some point.

# TODO:
# - Stuff to add
#	- convert to csv, txt is stupid and difficult

# imports
import matplotlib
import iso8601

print('Garden Automation System Weather Data Parser - 0.0.1A \n')

# open file
humidityData = open('humidityLog.txt')

# for loop to get data
# for (lines) get timestamp, value

# parse time
logItemTime = iso8601.parse_date(testLogFile.read())
# lineNumber = lineNumber+1(?)
# get values from col [x, x]

humidityData.close