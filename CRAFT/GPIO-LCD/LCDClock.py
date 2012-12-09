'''
Created on 20 Nov 2012

@author: Jamie
'''

import sys, time
from Daemon import Daemon
from datetime import datetime
from LCDLib import *

lcd_init()

class MyDaemon(Daemon):
    def run(self):
        oldSeconds = -1
        while True:
            now = datetime.now()
            seconds = now.second
            if seconds != oldSeconds:
                lcd_byte(LCD_LINE_1, LCD_CMD)
                lcd_string(datetime.now().strftime('%H:%M:%S'))
                lcd_byte(LCD_LINE_2, LCD_CMD)
                lcd_string(datetime.now().strftime('%a %d %b %y'))
            time.sleep(0.25)
            oldSeconds = seconds

if __name__ == "__main__":
    daemon = MyDaemon('/tmp/LCDClock.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)