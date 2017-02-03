'''
Created on 15 Nov 2012

@author: Jamie
'''
import threading
import smbus
from time import sleep 

bus = smbus.SMBus(0)
address = 0x20 # I2C address of MCP23017
iodirA = 0x00 # Register for Bank A I/O Direction
iodirB = 0x01 # Register for Bank B I/O Direction
gpioA = 0x12 # Register for Bank A GPIO
gpioB = 0x13 # Register for Bank B GPIO

address = 0x20 # I2C address of MCP23017
bus.write_byte_data(address, iodirA, 0x00) # Set all of bank A to outputs 
bus.write_byte_data(address, iodirB, 0xff) # Set all of bank B to inputs 

# GPIOA0 - Red
# GPIOA1 - Amber
# GPIOA2 - Green
# GPIOA3 - Buzzer
# GPIOA4 - Ped Red
# GPIOA5 - Ped Green

# GPIOB0 - Button

delayOnWalk = 4;
intraChangeDelay = 1
delayButtonServicing = 0.2

def sequenceLights():
    bus.write_byte_data(address, gpioA, 0x12)
    sleep(intraChangeDelay)
    bus.write_byte_data(address, gpioA, 0x29)
    sleep(delayOnWalk)
    bus.write_byte_data(address, gpioA, 0x2A)
    sleep(intraChangeDelay)
    bus.write_byte_data(address, gpioA, 0x14)
    sleep(intraChangeDelay)

try:
    bus.write_byte_data(address, gpioA, 0x14)
    while True:
        mybutton = bus.read_byte_data(address,0x13)
        if mybutton == False:
            sequenceLights()
            sleep(delayButtonServicing)
        
        
            
except KeyboardInterrupt:
    print "Caught Keyboard"
    bus.write_byte_data(address, gpioA, 0x00)
    
    
