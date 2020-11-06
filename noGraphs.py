# logs data in txt file, every hour
# might port to mongoDB or something in future
# manually set frequency  to water plants
# it's like the same thing w/o flask graphs

# TODO:
# - add stuff:
#       - saves data with mongoDB or txt file
#       - setup relay0 for watering plants
#       - manual control
#		- if waterInterval is set to something that isn't an integer, ask again
# - test everything

# imports
from gpiozero import LED, DigitalInputDevice  # controls rpi gpio, reads yl69 sensor
import time
import board 
import adafruit_dht # read DHT11 data

# vars
waterInterval = input('waterIntervals (hours) ' * 3600) # 3600s in hour

relay0 = LED(26) # these are gpio, not board pins
relay1 = LED(20)
relay2 = LED(21)

# yl69/fc28 sensor
soilMoistureSensor0 = DigitalInputDevice(4) # change 4 to whatever pin is in use
# will have at least 3 of these, maybe 6(?). figure out which pins

app = Flask(__name__)

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
	if (not soilMoistureSensor0.value):
		print('Level OK')
	
	else:
		# run function to activate relay
		print('Level Low')
		activateRelay0()

# get temp and humidity from tempSensor0
while True:
	try:
		print('temp =' + temp0) # change these to print to page
		print('humidity =' + humidity0)
	
	except RuntimeError as error:
		print(error.args[0]) # these sensors make errors often

	# getting data from sensors too often results in a lot of errors and bad readings
	sleep(tempSensorSleepTime)

# functions for scheduling watering
def waterSchedule():
	activateRelay0()
	sleep(int(waterInterval)) # set to int just in case

