'''
Created on 18 Dec 2012

@author: Jamie
'''
import matplotlib
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
from matplotlib import pyplot 
from matplotlib.dates import date2num
import matplotlib.dates as mdates
import sqlite3

datestamps = []
temps = []
pressures = []

years    = mdates.YearLocator()   # every year
months   = mdates.MonthLocator()  # every month
days    = mdates.DayLocator()
hours   = mdates.HourLocator()
daysFmt = mdates.DateFormatter('%a %d %b %y')

conn = sqlite3.connect("/var/local/log/test.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

sql = 'SELECT datetime as "[timestamp]", temp, pressure FROM logging'
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
try:
    cursor.execute(sql)
    rows = cursor.fetchall()
finally:
    cursor.close()

for row in rows:
    datestamps.append(row[0])
    temps.append(row[1])
    pressures.append(row[2])

dates = date2num(datestamps)
fig = pyplot.figure()
plt0 = fig.add_subplot(111)
plt1 = fig.add_subplot(211)

plt0.spines['top'].set_color('none')
plt0.spines['bottom'].set_color('none')
plt0.spines['left'].set_color('none')
plt0.spines['right'].set_color('none')
plt0.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

plt1.plot_date(dates, temps, 'b-', xdate=True)
plt1.set_title("Temperature")
#ax.xlabel('Date/Time')
plt1.xaxis.set_major_locator(days)
plt1.xaxis.set_major_formatter(daysFmt)
plt1.set_ylabel('Deg C')

plt2 = fig.add_subplot(212)
plt2.plot_date(dates, pressures, 'g-', xdate=True)
plt2.set_title("Barometric Pressure")
plt2.set_ylabel('hPa')

plt2.xaxis.set_major_locator(days)
plt2.xaxis.set_major_formatter(daysFmt)
#plt2.xaxis.set_minor_locator(hours)
plt2.set_xlabel('Date')

fig.autofmt_xdate()
pyplot.savefig('tempplot.png')
pyplot.show()
