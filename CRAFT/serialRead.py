'''
Created on 9 Feb 2013

@author: jamie
'''

import serial
import sys

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
while 1:
    line = ser.readline()   # read a '\n' terminated line
    sys.stdout.write(line)
ser.close()