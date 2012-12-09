'''
Created on 10 Nov 2012

@author: Jamie
'''

import RPi.GPIO as GPIO
from time import sleep

buzzer=22
delay = .3

GPIO.setmode(GPIO.BOARD)
GPIO.setup (buzzer, GPIO.OUT)

try:
    while 1:
        GPIO.output (buzzer, True)
        sleep(delay)
        GPIO.output (buzzer, False)
        sleep(delay)
except KeyboardInterrupt:
    GPIO.output (buzzer, False)