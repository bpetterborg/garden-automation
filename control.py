# Controls irrigation system for garden, using
# a Raspberry Pi.


# TODO:
#  - write GUI frontend (probably in Flask)
#  - add support for: 
#       - reading temperatures (DHT11 or something)
#       - reading humidity
#       - reading water barrel level
#  - add matplotlib graphs

# importing stuff
from gpiozero import LED  # controls rpi gpio
from time import sleep
import Flask # web frontend
import Adafruit_DHT # read DHT11 data

# variables
relay0 = LED(26)
#relay1 = # figure out what pins these go to
#relay2 = 

tempSensor = Adafruit_DHT.DHT11 # set temp sensor type
tempSensePin = 4 # set temp sensor pin
humidity, temp = Adafruit_DHT.read_retry(tempSensor, tempSensePin)