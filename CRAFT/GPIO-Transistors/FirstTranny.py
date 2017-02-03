'''
Created on 2 Aug 2012

@author: Jamie
'''
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup (22, GPIO.OUT)

while 1:
    GPIO.output (22, True)
    sleep(1)
    GPIO.output (22, False)
    sleep(1)
