'''
Created on 3 Dec 2012

@author: Jamie
'''

import ConfigParser

config = ConfigParser.RawConfigParser()

config.set('DEFAULT', 'consumer_key', '4BicbEzcZdlkYtbxnrRXA')
config.set('DEFAULT', 'consumer_secret', 'TKhjX1lBOCgU45olleseULQZKiHE5fmrJx1WyOSe1W4')
config.set('DEFAULT', 'access_token_key', '914832799-Xl3zPWFvxPA7UJ74sjt5zpa6WkxZoqC6y3IF8vUk')
config.set('DEFAULT', 'access_token_secret', 'H2Vndxc2eutA3oTadCO9hYWMt9iRXt4c7GznmHShwQ')

with open('twitter.cfg', 'wb') as configfile:
    config.write(configfile)