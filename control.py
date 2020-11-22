#!/usr/bin/env python3

# garden automation system

# logs data in txt file, every hour
# manually set frequency  to water plants
# it's like the same thing w/o flask graphs

# TODO: (everything is finished)
# - add stuff:
#       - manual control
#		- if waterInterval is set to something that isn't an integer, ask again
# 		- replace anything using board pins with gpio pins
# - testing
# 

# imports
from gpiozero import LED, DigitalInputDevice  # controls rpi gpio, reads yl69 sensor
from time import sleep
import board # make it so this is unneeded
import adafruit_dht # read DHT11 data
import datetime # timestamps
import csv # working with csv

print('Garden Automation System - 0.0.1A \n')

# specify schedule
waterInterval = input('waterIntervals (H) ' * 3600) # 3600s same as 1h
tempThreshold = input('tempThreshould ')
wateringDuration = input('wateringDuration (s) ')

# gpio
relay0 = LED(26) # these are gpio, not board pins
relay1 = LED(20)
relay2 = LED(21)

# yl69/fc28 sensor
soilMoistureSensor0 = DigitalInputDevice(4) # change 4 to whatever pin is in use
# will have at least 3 of these, maybe 6(?). figure out which pins

# dht11 sensor
tempSensorSleepTime = 60 # don't read temp sensor too frequently, it will freak out
tempSensor0 = adafruit_dht.DHT11(board.D17) # change these to not use board pins,

temp0 = tempSensor0.temperature
humidity0 = tempSensor0.humidity

# specify time to run relays for (seconds)
relay0TimeOn = wateringDuration
relay1TimeOn = 120
relay2TimeOn = 120

# functions for running relays
def activateRelay0():
	print('activating relay0') # print fun stuff to the TTY
	relay0.on()
	sleep(relay0TimeOn)
	print('deactivating relay0')
	relay0.off()

# pump
def activateRelay1():
	print('activating relay1')
	relay1.on()
	sleep(relay1TimeOn)
	print('deactivating relay1')
	relay1.off()

# unused
def activateRelay2():
	print('activating relay2')
	relay0.on()
	sleep(relay2TimeOn)
	print('deactivating relay2')
	relay0.off()

# get moisture sensor info
while True:
	if (not soilMoistureSensor0.value): # nominal value
		print('Level OK')
	
	else: # degraded value
		# run function to activate relay
		print('Level Low')
		activateRelay0()

# get temp and humidity from tempSensor0
while True:
	try:
		# get current time
		currentTime = datetime.datetime.now().isoformat()

		print('temp0 =' + str(temp0))
		print('humidity0 =' + str(humidity0))

		# write data to csv file (weatherLog.csv)
		with open('weatherLog.csv', mode='w') as weatherData:

			# specify stuff
			weatherDataWrite = csv.writer(
				weatherData, 
				delimiter',', 
				quotechar='"',
				quoting=csv.QUOTE_MINIMAL
				)
			# write temp0
			weatherDataWrite.writerow([
				str(currentTime), 
				str(temp0)
				])

			# write humidity0 (may need to specify what line, col)
			weatherDataWrite.writerow([
				str(currentTime),
				str(humidity0)
			])

			sleep(int(tempSensorSleepTime))
		
	
	except RuntimeError as error:
		print(error.args[0]) # these sensors make errors often

	# getting data from sensors too often results in a lot of errors and bad readings
	sleep(int(tempSensorSleepTime))

while True:
	activateRelay0()
	sleep(int(waterInterval))
