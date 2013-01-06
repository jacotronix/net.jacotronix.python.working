
import matplotlib
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
from matplotlib import pyplot 
from matplotlib.dates import date2num
import matplotlib.dates as mdates
import sqlite3

# Data series
datestamps = []
temps = []
pressures = []

# Various formatters
# These will have to change as the volume of data to be plotted increases
# As the x-axis will become too cluttered
years    = mdates.YearLocator()   # every year
months   = mdates.MonthLocator()  # every month
days    = mdates.DayLocator()
hours   = mdates.HourLocator()
daysFmt = mdates.DateFormatter('%a %d %b %y')
monthsFmt = mdates.DateFormatter('%b %y')

# Connect to database
conn = sqlite3.connect("/var/local/log/test.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

# Set up SQL query and perform on the database
# Very poorly written 'exception' handling
sql = 'SELECT datetime as "[timestamp]", temp, pressure FROM logging'
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
try:
    cursor.execute(sql)
    rows = cursor.fetchall()
finally:
    cursor.close()

# Transfer SQL data into the data series
# Must be a better way to do this
for row in rows:
    datestamps.append(row[0])
    temps.append(row[1])
    pressures.append(row[2])

# Convert the dates into a format that matplotlib can handle
dates = date2num(datestamps)

# Create the figure and 2 sublots
fig = pyplot.figure()
plt0 = fig.add_subplot(111)
plt1 = fig.add_subplot(211)

# Hide all un-necessary adornments
plt0.spines['top'].set_color('none')
plt0.spines['bottom'].set_color('none')
plt0.spines['left'].set_color('none')
plt0.spines['right'].set_color('none')
plt0.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

# Plot Temperature sub-plot
plt1.plot_date(dates, temps, 'b-', xdate=True)
plt1.set_title("Temperature")
plt1.xaxis.set_major_locator(months)
plt1.xaxis.set_major_formatter(monthsFmt)
plt1.set_ylabel('Deg C')

# Plot Pressure sub-plot
plt2 = fig.add_subplot(212)
plt2.plot_date(dates, pressures, 'g-', xdate=True)
plt2.set_title("Barometric Pressure")
plt2.set_ylabel('hPa')

# Set x-axis label & format
plt2.xaxis.set_major_locator(months)
plt2.xaxis.set_major_formatter(monthsFmt)
plt2.set_xlabel('Date')
fig.autofmt_xdate()

# Save the the graph image
pyplot.savefig('weather-plot.png')
pyplot.show()
