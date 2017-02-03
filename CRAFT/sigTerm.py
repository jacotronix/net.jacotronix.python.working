'''
Created on 19 Jul 2012

@author: Jamie
'''

import signal
import sys

def signal_handler_term(signal, frame):
    print "Caught SIGTERM"
    sys.exit()

signal.signal(signal.SIGTERM, signal_handler_term)

try:
    while True:
        pass
except KeyboardInterrupt:
    print "Caught Keyboard"
