'''
Created on 10 Nov 2012

@author: Jamie
'''

import threading
from time import sleep
import RPi.GPIO as GPIO

pedRed=16   # GPIO4
buzzer=22   # GPIO6

flashes = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup (pedRed, GPIO.OUT)
GPIO.setup (buzzer, GPIO.OUT)

class ThreadBuzz ( threading.Thread ):
    def run ( self ):
        flasherTh = ThreadFlash()
        flasherTh.start()
        while flasherTh.isAlive():
            GPIO.output (buzzer, True)
            sleep(.3)
            GPIO.output (buzzer, False)
            sleep(.3)

class ThreadFlash ( threading.Thread ):
    def run ( self ):
        for null in range(flashes):
            GPIO.output (pedRed, False)
            sleep(1)
            GPIO.output (pedRed, True)
            sleep(1)

buzzerTh = ThreadBuzz()
buzzerTh.start()

GPIO.output (pedRed, True)
GPIO.output (buzzer, False)
