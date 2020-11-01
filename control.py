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
import board
import adafruit_dht # read DHT11 data

# variables
relay0 = LED(26)
#relay1 = # figure out what pins these go to
#relay2 = 

tempSensor = adafruit_dht.DHT11(board.D17)
tempSensorSleepTime = 2.0 # don't read temp sensor too frequently

while True:
    try:
        global temp
        global humidity
        temp = tempSensor.temperature
        humidity = tempSensor.humidity
        
        print('temp =' + temp) # change these to print to page
        print('humidity =' + humidity)
    
    except RuntimeError as error:
        print(error.args[0]) # these sensors make errors often

    time.sleep(tempSensorSleepTime)
