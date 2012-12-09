'''
Created on 3 Nov 2012

@author: Jamie
'''

import smbus
from time import sleep 
bus = smbus.SMBus(0)

address = 0x20 # I2C address of MCP23017
iodirA = 0x00 # Register for Bank A I/O Direction
gpioA = 0x12 # Register for Bank A GPIO

bus.write_byte_data(address, iodirA, 0x00) # Set all of bank A to outputs 

sequence = [0x01, 0x03, 0x04, 0x02]

try:
    while 1:
        for pos in sequence:
            bus.write_byte_data(address, gpioA, pos)
            sleep(1)
except KeyboardInterrupt:
    print "Caught Keyboard"
    bus.write_byte_data(address, gpioA, 0x00)