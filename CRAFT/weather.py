'''
Created on 7 Jun 2014

@author: Jamie
'''
import pywapi
import pprint
import string
import sys
import datetime

weather_com_result = pywapi.get_weather_from_weather_com('UKXX1087')
kphToMph = 1.60934400061

dayOfWeek = {}
high = {}
low = {}
precip = {}
winSpd = {}
winDir = {}

#print string.lower(weather_com_result['current_conditions']['text']) + ""

start = 0
try:
    test = int(weather_com_result['forecasts'][0]['day']['wind']['speed'])
except ValueError:
    start = 1

for i in range(start, 5):
    
    dayOfWeek[i] = weather_com_result['forecasts'][i]['day_of_week']
    high[i] = weather_com_result['forecasts'][i]['high']
    low[i] = weather_com_result['forecasts'][i]['low']
    precip[i] = weather_com_result['forecasts'][i]['day']['chance_precip']
    winSpd[i] = "{:.0f}".format(int(weather_com_result['forecasts'][i]['day']['wind']['speed'])  / kphToMph)
    winDir[i] = weather_com_result['forecasts'][i]['day']['wind']['text']
    
windSpeed = int(weather_com_result['current_conditions']['wind']['speed']) / kphToMph
curr_wind = "{:.0f}mph ".format(windSpeed) + weather_com_result['current_conditions']['wind']['text']
curr_temp = weather_com_result['current_conditions']['temperature'] + u'\N{DEGREE SIGN}' + "C"
curr_press = weather_com_result['current_conditions']['barometer']['reading'] + " mb"
today = weather_com_result['forecasts'][0]['day_of_week'][0:3] + " " + weather_com_result['forecasts'][0]['date'][4:] \
    + " " + weather_com_result['forecasts'][0]['date'][:3]
uv = weather_com_result['current_conditions']['uv']['text']
humid = weather_com_result['current_conditions']['humidity']

print today
print curr_temp
print curr_wind
print curr_press
print "UV {}".format(uv)
print "Hum {}%".format(humid)

dayrow = "\t"
highRow = "High\t"
lowRow = "Low\t"
precipRow = "Rain\t"
windRow = "Wind\t"
for i in dayOfWeek:
    dayrow += (dayOfWeek[i][0:3] + "\t")
    highRow += (high[i] + u'\N{DEGREE SIGN}' + "C" + "\t")
    lowRow += (low[i] + u'\N{DEGREE SIGN}' + "C" + "\t")
    precipRow += (precip[i] + "%\t")
    windRow += (winDir[i] + winSpd[i] + "\t")

print dayrow
print highRow
print lowRow
print precipRow
print windRow
    
pp = pprint.PrettyPrinter(indent=4)

#kalamata = pywapi.get_weather_from_weather_com('UKXX1087')

pp.pprint(weather_com_result)