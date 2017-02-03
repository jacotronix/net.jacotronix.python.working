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

while 1:
    GPIO.output (11, False)
    GPIO.output (12, False)
    GPIO.output (13, False)
    sleep(1)
    GPIO.output (11, True)
    GPIO.output (12, True)
    GPIO.output (13, True)
    sleep(1)