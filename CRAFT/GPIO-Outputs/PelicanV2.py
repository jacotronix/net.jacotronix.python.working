'''
Created on 10 Nov 2012

@author: Jamie
'''

import threading
from time import sleep
import RPi.GPIO as GPIO

red=11      # GPIO0
yellow=12   # GPIO1
green=13    # GPIO2
button=15   # GPIO3
pedRed=16   # GPIO4
pedGreen=18 # GPIO5
buzzer=22   # GPIO6

flashes = 5
delayOnGreen = 4;
delayFlashingAmber = 0.5
delayBuzzer = 0.3
delayButtonServicing = 0.2

# Setup board & pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup (red, GPIO.OUT)
GPIO.setup (yellow, GPIO.OUT)
GPIO.setup (green, GPIO.OUT)
GPIO.setup (button, GPIO.IN)
GPIO.setup (pedRed, GPIO.OUT)
GPIO.setup (pedGreen, GPIO.OUT)
GPIO.setup (buzzer, GPIO.OUT)

# Starting state for LEDs
GPIO.output (red, True)
GPIO.output (yellow, True)
GPIO.output (green, False)
GPIO.output (pedRed, False)
GPIO.output (pedGreen, True)

# Thread to sequence LEDs through red & flashing amber
# whilst buzzer sounding
class ThreadLights ( threading.Thread ):
    def run ( self ):
        # Red / Walk 
        GPIO.output (red, False)
        GPIO.output (yellow, True)
        GPIO.output (green, True)
        GPIO.output (pedRed, True)
        GPIO.output (pedGreen, False)
        sleep(delayOnGreen)
        # Flashing Amber
        GPIO.output (red, True)
        GPIO.output (green, True)
        for null in range(flashes):
            GPIO.output (yellow, False)
            GPIO.output (pedGreen, False)
            sleep(delayFlashingAmber)
            GPIO.output (yellow, True)
            GPIO.output (pedGreen, True)
            sleep(delayFlashingAmber)

def sequenceLights():
    # Amber        
    GPIO.output (red, True)
    GPIO.output (yellow, False)
    GPIO.output (green, True)
    sleep(2)
    # Start red / flashing amber thread
    lightsTh = ThreadLights()
    lightsTh.start()
    # Sound buzzer while thread is alive
    while lightsTh.isAlive():
        GPIO.output (buzzer, True)
        sleep(delayBuzzer)
        GPIO.output (buzzer, False)
        sleep(delayBuzzer)
    #Green / Buzzer Off
    GPIO.output (red, True)
    GPIO.output (yellow, True)
    GPIO.output (green, False)
    GPIO.output (pedRed, False)
    
try:
    while True:
        # Service the buzzer
        # (Interrupts would be better)
        # (DOn't think they work on RPi GPIO yet)
        buttonReading = GPIO.input(button)
        if buttonReading == False:
            sequenceLights()
            sleep(delayButtonServicing)
# Catch ctrl-C on keyboard and turn the LEDs off
except KeyboardInterrupt:
    GPIO.output (red, True)
    GPIO.output (yellow, True)
    GPIO.output (green, True)
    GPIO.output (pedRed, True)
    GPIO.output (pedGreen, True)

