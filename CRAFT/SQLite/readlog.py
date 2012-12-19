'''
Created on 18 Dec 2012

@author: Jamie
'''
import matplotlib
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
from matplotlib import pyplot 
from matplotlib.dates import date2num
import sqlite3

datestamps = []
temps = []
pressures = []


conn = sqlite3.connect("test.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

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

#------------------------------

dates = date2num(datestamps)
pyplot.plot_date(dates, temps, 'b-', xdate=True)
pyplot.plot_date(dates, pressures, 'g-', xdate=True)
pyplot.title('Temperatures')
pyplot.xlabel('Date/Time')
pyplot.ylabel('Temp Deg C')
pyplot.savefig('tempplot.png')
pyplot.show()

#http://stackoverflow.com/questions/7340547/multiple-data-set-plotting-with-matplotlib-pyplot-plot-date
#
#http://matplotlib.org/examples/api/two_scales.html
#
#http://klassenresearch.orbs.com/Plotting+with+Python
#
#http://matplotlib.org/users/pyplot_tutorial.html
#
#http://www.endlesslycurious.com/2011/05/04/basic-graphing-with-matplotlib/
#
#http://matplotlib.org/api/pyplot_api.html?highlight=plot_date#matplotlib.pyplot.plot_date
 

