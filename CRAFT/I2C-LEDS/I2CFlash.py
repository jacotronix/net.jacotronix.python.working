'''
Created on 3 Nov 2012

@author: Jamie
'''

import smbus
from time import sleep 
bus = smbus.SMBus(0)

address = 0x20 # I2C address of MCP23017
bus.write_byte_data(0x20,0x00,0x00) # Set all of bank A to outputs 
bus.write_byte_data(0x20,0x01,0x00) # Set all of bank B to outputs 

try:
    while 1:
        bus.write_byte_data(address,0x12,0x07)
        sleep(1)
        bus.write_byte_data(address,0x12,0x00)
        sleep(1)
except KeyboardInterrupt:
    print "Caught Keyboard"
    bus.write_byte_data(address,0x12,0x00)