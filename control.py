# Controls irrigation system for garden, using
# a Raspberry Pi, outputs data to flask frontend

# TODO:
#  - finish writing GUI frontend for flask
#  - add features: 
#       - reading water storage level
#       - reading soil moisture levels
#       - manual watering mode
#       - remotely setting relayXTimeOn
#  - add matplotlib graphs, display in flask with pyplot
#  - test everything, on RPi

# importing stuff for displaying data
from flask import Flask, render_template # web frontend
import matplotlib.pyplot as plot # pyplot graphing  (still need to install)
import numpy # math stuff

# importing stuff for sensors
from gpiozero import LED, DigitalInputDevice  # controls rpi gpio
import time
import board 
import adafruit_dht # read DHT11 data

# variables
# relay pins
relay0 = LED(26) # these are gpio, not board pins
relay1 = LED(20)
relay2 = LED(21)

# time to open relays for (s)
relay0TimeOn = 120 # solenoid (set correct values)
relay1TimeOn = 120 # pump
relay2TimeOn = 120 # unused

# yl69/fc28 sensor
soilMoistureSensor0 = DigitalInputDevice(4) # change 4 to whatever pin is in use
# will have at least 3 of these, maybe 6(?). figure out which pins

app = Flask(__name__)

# dht11 sensor
tempSensorSleepTime = 2.0 # don't read temp sensor too frequently, it will freak out

tempSensor0 = adafruit_dht.DHT11(board.D17) # change these to not use board pins
#tempSensor1 = adafruit_dht.DHT11(board D17)

temp0 = tempSensor0.temperature
humidity0 = tempSensor0.humidity

# relay control (3ch)
# solenoid
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

# get soil moisture levels
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

# pyplot things
# use a for loop to fetch past 48 hours of data
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plot.show()


# print data to page
@app.route('/')
def home():
    
    # print data
    return temp
    # add soil moisture sensor state
    # add matplotlib graphs

# print graphs to page (pyplot)
#def graphs():

if __name__ == '__main__':
    app.run(host = '0.0.0.0')