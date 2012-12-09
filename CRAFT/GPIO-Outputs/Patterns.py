'''
Created on 10 Nov 2012

@author: Jamie
'''
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
GPIO.setup (12, GPIO.OUT)
GPIO.setup (13, GPIO.OUT)
GPIO.output (11, True)
GPIO.output (12, True)
GPIO.output (13, True)

sequence = [[0, 0, 1],
            [0, 1, 0],
            [1, 0, 0]]
try:
    while 1:
        for line in sequence:
            for i in range(len(line)):
                op = (True, False)[line[i]==1]
                GPIO.output (13-i, op)
            sleep(0.5)
except KeyboardInterrupt:
    print ("Caught Keyboard")
    GPIO.output (11, True)
    GPIO.output (12, True)
    GPIO.output (13, True)