'''
Created on 3 Dec 2012

@author: Jamie
'''
import ConfigParser

config = ConfigParser.RawConfigParser()
try:
    config.readfp(open('twitter.cfg'))
except IOError as e:
    print "I/O error ({0}): ({1})".format(e.errno, e.strerror)
    exit(1)

username = config.get('Twitter', 'username')
password = config.get('Twitter', 'password')
try:
    poo1 = config.get('poo', 'poo')
except ConfigParser.NoSectionError as e:
    print "NoSectionError"
try:
    poo2 = config.get('Twitter', 'poo')
except ConfigParser.NoOptionError as e:
    print "NoOptionError"

print username
print password