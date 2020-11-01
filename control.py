# Controls irrigation system for garden, using
# a Raspberry Pi.

# TODO:
#  - write GUI frontend (probably in Flask)
#  - add support for: 
#       - reading water storage level
#  - add matplotlib graphs in flask

# importing stuff
from gpiozero import LED  # controls rpi gpio
from time import sleep
from flask import Flask, render_template # web frontend
import board
import adafruit_dht # read DHT11 data

# variables
relay0 = LED(26)
#relay1 = # figure out what pins these go to
#relay2 = 
app = Flask(__name__)

tempSensor = adafruit_dht.DHT11(board.D17)
tempSensorSleepTime = 2.0 # don't read temp sensor too frequently

# get temp and humidity
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

# print data to page
@app.route('/')
def home():
    
    # print data
    return temp
    return humidity
    # add matplotlib graphs


if __name__ == '__main__':
    app.run()
    