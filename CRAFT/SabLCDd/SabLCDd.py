'''
Created on 17 Jul 2012

@author: Jamie
'''

import signal
import sys
import urllib
import xml.etree.ElementTree as xml
import socket
from time import sleep

def signal_handler_term(signal, frame):
    print "Caught SIGTERM"
    sys.exit()

signal.signal(signal.SIGTERM, signal_handler_term)

sabStatusUrl="http://192.168.2.149:2708/sabnzbd/api?mode=queue&start=START&limit=LIMIT&output=xml&apikey=4336109f0d490023a8cc9e1be2b635a2"
lcdIP='192.168.2.49'
lcdPort=13666

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((lcdIP, lcdPort))

sock.send("hello\n")
#print sock.recv(1024)

sock.send("client_set name sabClient\n")
#print sock.recv(1024)
sock.send("screen_add sabSCR\n")
#print sock.recv(1024)
sock.send("widget_add sabSCR one string\n")
sock.send("widget_add sabSCR two string\n")
sock.send("widget_add sabSCR three string\n")
sock.send("widget_add sabSCR four string\n")
#print sock.recv(1024)

try:
    while 1:
        rss = xml.parse(urllib.urlopen(sabStatusUrl)).getroot()
    
        element = rss.find('noofslots')
        queue = element.tag + ": " + element.text
        element = rss.find('kbpersec')
        rate = element.tag + ": " + element.text
        element = rss.find('timeleft')
        timeleft = element.tag + ": " + element.text
        element = rss.find('sizeleft')
        sizeleft = element.tag + ": " + element.text
        line1str="widget_set sabSCR one 1 1 {" + rate + "}\n"
        line2str="widget_set sabSCR two 1 2 {" + queue + "}\n"
        line3str="widget_set sabSCR three 1 3 {" + timeleft + "}\n"
        line4str="widget_set sabSCR four 1 4 {" + sizeleft + "}\n"
        sock.send(line1str)
        sock.send(line2str)
        sock.send(line3str)
        sock.send(line4str)
        #print sock.recv(1024)
        sleep(3)

except KeyboardInterrupt:
    print "Caught Keyboard"
    sock.close( )
    