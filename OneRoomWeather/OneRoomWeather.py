'''
Created on 7 Dec 2012

@author: Jamie
'''
import sys, time, syslog
from datetime import datetime, timedelta
import smbus
import sqlite3

from daemon import *
from RPiCharLCD import *
import BMP085
import tweeter

# Open syslog
syslog.openlog(logoption=syslog.LOG_PID)

# Create a tweeter object
myTweeter = tweeter.tweeter()

# Create I2C bus & BMP085 Objects
i2c = smbus.SMBus(0)
sensor = BMP085.BMP085(i2c, 0x77)

# Create SQLite database connection 
conn = sqlite3.connect("/var/local/log/test.db",
                       detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

# Create database cursor and create table if it doesn't exist 
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS logging (datetime TIMESTAMP, temp FLOAT, pressure INT)')

# Initialise the LCD display
myLCD = RPiCharLCD()
myLCD.lcd_init()

# Inherit from Daemon class
class MyDaemon(daemon):
    # implement run method
    def run(self):
        
        # record event times
        lastTimeUpd = datetime.now()
        lastSensorReading = datetime.now()
        lastTweet = datetime.now()
        lastLog = datetime.now()
        
        #initialise temperature and pressure
        t = None
        p = None
        
        # main loop
        while True:
            
            # Calculate elapsed time since last events
            now = datetime.now()
            timeElapsed = now - lastTimeUpd
            sensorElapsed = now - lastSensorReading
            tweetElapsed = now - lastTweet
            logElapsed = now - lastLog
            
            # Time to read temp & pressure
            if sensorElapsed > timedelta(seconds=5):
                t = sensor.readTemperature()
                p = (sensor.readPressure()/100)
#                myLCD.lcd_byte(myLCD.LCD_LINE_2, myLCD.LCD_CMD)
#                myLCD.lcd_string("{0!s} C {1!s} hPa".format(t, p))                
                myLCD.lcd_write_string("{0!s} C {1!s} hPa".format(t, p), 2)                
                lastSensorReading = now
            
            # Time to log to database
            if logElapsed > timedelta(hours=1):
                c.execute('INSERT INTO logging VALUES(?, ?, ?)', (now, t, p))
                conn.commit()
                lastLog = now

            # Time to tweet
            if tweetElapsed > timedelta(minutes=10):
                try:
                    myTweeter.tweet(datetime.now().strftime('%a %d %b %y %H:%M .. ') +
                                    "{0!s} C .. {1!s} hPa".format(t, p))
                except Exception as e:
                    pass
                lastTweet = now
            
            # Time to update LCD Display
            if timeElapsed > timedelta(seconds=1):
                myLCD.lcd_byte(myLCD.LCD_LINE_1, myLCD.LCD_CMD)
                myLCD.lcd_write_string(datetime.now().strftime('%H:%M:%S'), 1)
                lastTimeUpd = now
                
            time.sleep(0.3)


if __name__ == "__main__":
    daemon = MyDaemon('/tmp/LCDClock.pid', stdout='/tmp/clockout.log', stderr='/tmp/clockerr.log')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            syslog.syslog(syslog.LOG_INFO, "Starting")
            daemon.start()
        elif 'stop' == sys.argv[1]:
            syslog.syslog(syslog.LOG_INFO, "Stopping")
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            syslog.syslog(syslog.LOG_INFO, "Restarting")
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)