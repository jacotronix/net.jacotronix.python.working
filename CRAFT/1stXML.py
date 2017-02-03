'''
Created on 16 Jul 2012

@author: Jamie
'''
import urllib
import xml.etree.ElementTree as xml

url="http://192.168.2.149:2708/sabnzbd/api?mode=queue&start=START&limit=LIMIT&output=xml&apikey=4336109f0d490023a8cc9e1be2b635a2"

#handle = urllib.urlopen(url)
#print handle.read()

rss = xml.parse(urllib.urlopen(url)).getroot()

xml.dump(rss)

for element in rss.findall('categories/category'):
    print element.text

print

for element in rss.findall('slots/slot/filename'):
    print element.text

print

element = rss.find('uptime')
print element.tag + ": " + element.text

element = rss.find('kbpersec')
print element.tag + ": " + element.text

element = rss.find('noofslots')
print element.tag + ": " + element.text

element = rss.find('paused')
print element.tag + ": " + element.text

print

