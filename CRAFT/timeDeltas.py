'''
Created on 7 Dec 2012

@author: Jamie
'''
from datetime import datetime, timedelta
import time

oldNow = datetime.now()

while True:
    now = datetime.now()
    elapsed = now - oldNow
    if elapsed > timedelta(seconds=5):
        print "tick"
        oldNow = now
    time.sleep(0.3)
