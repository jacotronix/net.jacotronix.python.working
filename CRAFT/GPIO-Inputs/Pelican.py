'''
Created on 10 Nov 2012

@author: Jamie
'''

import RPi.GPIO as GPIO
from time import sleep

red=11      # GPIO0
yellow=12   # GPIO1
green=13    # GPIO2
button=15   # GPIO3
pedRed=16   # GPIO4
pedGreen=18 # GPIO5
buzzer=22   # GPIO6

flashes = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup (red, GPIO.OUT)
GPIO.setup (yellow, GPIO.OUT)
GPIO.setup (green, GPIO.OUT)
GPIO.setup (button, GPIO.IN)
GPIO.setup (pedRed, GPIO.OUT)
GPIO.setup (pedGreen, GPIO.OUT)
GPIO.setup (buzzer, GPIO.OUT)

GPIO.output (red, True)
GPIO.output (yellow, True)
GPIO.output (green, False)
GPIO.output (pedRed, False)
GPIO.output (pedGreen, True)


def sequenceLights():
    # Amber        
    GPIO.output (red, True)
    GPIO.output (yellow, False)
    GPIO.output (green, True)
    sleep(2)
    # Red / Walk
    GPIO.output (red, False)
    GPIO.output (yellow, True)
    GPIO.output (green, True)
    GPIO.output (pedRed, True)
    GPIO.output (pedGreen, False)
    sleep(4)
    # Flashing Amber
    GPIO.output (red, True)
    GPIO.output (green, True)
    for null in range(flashes):
        GPIO.output (yellow, False)
        GPIO.output (pedGreen, False)
        sleep(.5)
        GPIO.output (yellow, True)
        GPIO.output (pedGreen, True)
        sleep(.5)
    #Green
    GPIO.output (red, True)
    GPIO.output (yellow, True)
    GPIO.output (green, False)
    GPIO.output (pedRed, False)
    
try:
    while True:
        buttonReading = GPIO.input(button)
        if buttonReading == False:
            sequenceLights()
            sleep(.2)
except KeyboardInterrupt:
    GPIO.output (red, True)
    GPIO.output (yellow, True)
    GPIO.output (green, True)
    GPIO.output (pedRed, True)
    GPIO.output (pedGreen, True)

