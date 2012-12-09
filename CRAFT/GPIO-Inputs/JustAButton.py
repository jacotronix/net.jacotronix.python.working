'''
Created on 9 Nov 2012

@author: Jamie
'''
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(15, GPIO.IN)

while True:
    mybutton = GPIO.input(15)
    if mybutton == False:
        print "Charlie!!"
        time.sleep(.2)