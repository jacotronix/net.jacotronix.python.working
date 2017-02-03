'''
Created on 3 Dec 2012

@author: Jamie
'''
import ConfigParser

config = ConfigParser.RawConfigParser()

config.set('DEFAULT', 'pish', 'pish')
config.add_section('Twitter')
config.set('Twitter', 'username', 'mytwitter')
config.set('Twitter', 'password', '12345678')

with open('twitter.cfg', 'wb') as configfile:
    config.write(configfile)