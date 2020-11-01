# Controls irrigation system for garden, using
# a Raspberry Pi.

# TODO:
#  - add some code
#  - write GUI frontend (probably in Flask)
#  - add support for: 
#       - reading temperatures
#       - reading humidity
#       - reading water barrel level

# importing stuff
from gpiozero import LED as relay # controls rpi gpio
from time import sleep
import Flask # web frontend

# variables
relay0 = relay(26)
#relay1 = # figure out what pins these go to
#relay2 = 