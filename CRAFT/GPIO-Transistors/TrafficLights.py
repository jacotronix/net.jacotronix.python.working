'''
Created on 27 Oct 2012

@author: Jamie
'''

import RPi.GPIO as GPIO
from time import sleep

red=11
yellow=12
green=13

GPIO.setmode(GPIO.BOARD)
GPIO.setup (red, GPIO.OUT)
GPIO.setup (yellow, GPIO.OUT)
GPIO.setup (green, GPIO.OUT)

try:
    while True:
        GPIO.output (red, True)
        GPIO.output (yellow, False)
        GPIO.output (green, False)
        sleep(2)
        GPIO.output (red, True)
        GPIO.output (yellow, True)
        GPIO.output (green, False)
        sleep(2)
        GPIO.output (red, False)
        GPIO.output (yellow, False)
        GPIO.output (green, True)
        sleep(2)
        GPIO.output (red, False)
        GPIO.output (yellow, True)
        GPIO.output (green, False)
        sleep(2)
except KeyboardInterrupt:
    GPIO.output (red, False)
    GPIO.output (yellow, False)
    GPIO.output (green, False)