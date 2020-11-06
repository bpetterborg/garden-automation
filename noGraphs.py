# garden automation system, without flask and  matplotlib

# logs data in txt file, every hour
# might port to mongoDB or something in future
# manually set frequency  to water plants
# it's like the same thing w/o flask graphs

# TODO:
# - add stuff:
#       - log data to txt
#       - setup relay0 for watering plants
#       - manual control
#		- if waterInterval is set to something that isn't an integer, ask again
# - test everything

# imports
from gpiozero import LED as, DigitalInputDevice  # controls rpi gpio, reads yl69 sensor
import time
import board 
import adafruit_dht # read DHT11 data

print('Garden Automation System - A 0.0.1 \n')


# vars
waterInterval = input('waterIntervals (hours) ' * 3600) # 3600s in hour
tempThreshold = input('tempThreshould ')

relay0 = LED(26) # these are gpio, not board pins
relay1 = LED(20)
relay2 = LED(21)

# yl69/fc28 sensor
soilMoistureSensor0 = DigitalInputDevice(4) # change 4 to whatever pin is in use
# will have at least 3 of these, maybe 6(?). figure out which pins

# dht11 sensor
tempSensorSleepTime = 2.0 # don't read temp sensor too frequently, it will freak out
tempSensor0 = adafruit_dht.DHT11(board.D17) # change these to not use board pins,

temp0 = tempSensor0.temperature
humidity0 = tempSensor0.humidity

# specify time to run relays for (seconds)
relay0TimeOn = 120 
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
		print('temp0 =' + temp0) # change these to print to page
		print('humidity0 =' + humidity0)
	
	except RuntimeError as error:
		print(error.args[0]) # these sensors make errors often

	# getting data from sensors too often results in a lot of errors and bad readings
	sleep(tempSensorSleepTime)

while True:
	activateRelay0()
	sleep(int(waterInterval))