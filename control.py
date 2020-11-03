# Controls irrigation system for garden, using
# a Raspberry Pi, outputs data to flask frontend

# TODO:
#  - finish writing GUI frontend for flask
#  - add features: 
#       - reading water storage level
#       - reading soil moisture levels
#       - manual mode
#       - remotely setting of relayXTimeOn
#  - add matplotlib graphs, display in flask
#  - test everything, on RPi

# importing stuff
from gpiozero import LED, DigitalInputDevice  # controls rpi gpio
from time import sleep
from flask import Flask, render_template # web frontend
import board
import adafruit_dht # read DHT11 data

# variables
relay0 = LED(26)
relay1 = LED(20)
relay2 = LED(21)
relay0TimeOn = 120 # solenoid (set correct values)
relay1TimeOn = 120 # pump
relay2TimeOn = 120 # unused

# yl69/fc28 sensor
soilMoistureSensor0 = DigitalInputDevice(4) # change 4 to whatever pin is in use
# will have at least 3 of these, maybe 6(?)

app = Flask(__name__)

# dht11 sensor
tempSensor = adafruit_dht.DHT11(board.D17)
tempSensorSleepTime = 2.0 # don't read temp sensor too frequently
temp = tempSensor.temperature
humidity = tempSensor.humidity

# relay control (3ch)
def activateRelay0():
    print('activating relay0')
    relay0.on()
    sleep(relay0TimeOn)
    print('deactivating relay0')
    relay0.off()

def activateRelay1():
    print('activating relay1')
    relay1.on()
    sleep(relay1TimeOn)
    print('deactivating relay1')
    relay1.off()

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

# get temp and humidity
while True:
    try:
        print('temp =' + temp) # change these to print to page
        print('humidity =' + humidity)
    
    except RuntimeError as error:
        print(error.args[0]) # these sensors make errors often

    time.sleep(tempSensorSleepTime)

# print data to page
@app.route('/')
def home():
    
    # print data
    return temp
    return humidity
    # add matplotlib graphs

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
    