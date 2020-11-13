#!/usr/bin/env python3

# garden automation system

# logs data in txt file, every hour
# might port to mongoDB or something in future
# manually set frequency  to water plants
# it's like the same thing w/o flask graphs

# TODO:
# - add stuff:
#       - manual control
#		- if waterInterval is set to something that isn't an integer, ask again
# - test everything

# imports
from gpiozero import LED, DigitalInputDevice  # controls rpi gpio, reads yl69 sensor
from time import sleep
import board # make it so this is unneeded
import adafruit_dht # read DHT11 data
import datetime # timestamps

print('Garden Automation System - 0.0.1A \n')

# specify schedule
waterInterval = input('waterIntervals (hours) ' * 3600) # 3600s in hour
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
tempSensorSleepTime = 3600 # don't read temp sensor too frequently, it will freak out
tempSensor0 = adafruit_dht.DHT11(board.D17) # change these to not use board pins,

temp0 = tempSensor0.temperature
humidity0 = tempSensor0.humidity

# specify time to run relays for (seconds)
relay0TimeOn = wateringDuration
relay1TimeOn = 120
relay2TimeOn = 120

# complain if waterInterval or tempThreshould is not an int of flt

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

		print('temp0 =' + str(temp0)) # change these to print to page
		print('humidity0 =' + str(humidity0))

		# data logging (humidity0)
		humidityLogFile = open('humidityLog.txt', 'a')
		humidityLogFile.write('\n' + str(currentTime) + str(humidity0)) # add timestamp
		humidityLogFile.close() # close file

		# data logging (temp0)
		tempLogFile = open('tempLog.txt', 'a')
		tempLogFile.write('\n' + str(currentTime) + str(temp0)) # add timestamp
		tempLogFile.close()
	
	except RuntimeError as error:
		print(error.args[0]) # these sensors make errors often

	# getting data from sensors too often results in a lot of errors and bad readings
	sleep(tempSensorSleepTime)

while True:
	activateRelay0()
	sleep(int(waterInterval))
