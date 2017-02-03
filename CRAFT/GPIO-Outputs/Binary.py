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

try:
    while 1:
        i = 0
        while i <= 7:
            j = 0
            while j<3:
                GPIO.output(11+j, ((True, False)[((i&(1<<j))>0)]))
                j=j+1
            i=i+1
            sleep(1)
except KeyboardInterrupt:
    print ("Caught Keyboard")
    GPIO.output (11, True)
    GPIO.output (12, True)
    GPIO.output (13, True)