'''
Created on 15 Nov 2012

@author: Jamie
'''

import smbus
from time import sleep 
bus = smbus.SMBus(0)

address = 0x20 # I2C address of MCP23017
bus.write_byte_data(0x20,0x00,0x00) # Set all of bank A to outputs 
bus.write_byte_data(0x20,0x01,0x01) # Set all of bank B to outputs 

while True:
    mybutton = bus.read_byte_data(address,0x13)

    if mybutton == False:
        print "Ouch!!"
        bus.write_byte_data(address, 0x13, 0x02)
    else:
        print "Eeek!!"
        bus.write_byte_data(address, 0x13, 0x00)
    sleep(1)