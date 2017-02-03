'''
Created on 10 Nov 2012

@author: Jamie
'''

import threading
from time import sleep

flashes = 5

class ThreadBuzz ( threading.Thread ):
    def run ( self ):
        print 'Thread', self.getName(), 'started.'
        flasher = ThreadFlash()
        flasher.start()
        while flasher.isAlive():
            print "Flash is Alive!"
            print "Buzz"
            sleep(.4)
        print 'Thread', self.getName(), 'ended.'

class ThreadFlash ( threading.Thread ):
    def run ( self ):
        print 'Thread', self.getName(), 'started.'
        for null in range(flashes):
            print "Flash!"
            sleep(1)
        print 'Thread', self.getName(), 'ended.'

buzzer = ThreadBuzz()
buzzer.start()
