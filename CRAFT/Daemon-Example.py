'''
Created on 20 Nov 2012

@author: Jamie
'''
#!/usr/bin/env python

# Logging levels:
# LOG_EMERG
# LOG_ALERT
# LOG_CRIT
# LOG_ERR
# LOG_WARNING
# LOG_NOTICE
# LOG_INFO
# LOG_DEBUG.

import sys, time, syslog
from Daemon import Daemon

syslog.openlog(logoption=syslog.LOG_PID)

class MyDaemon(Daemon):
    def run(self):
        while True:
            time.sleep(1)
            syslog.syslog(syslog.LOG_ERR, 'Ouch....')

if __name__ == "__main__":
    daemon = MyDaemon('/tmp/daemon-example.pid')
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