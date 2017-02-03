'''
Created on 3 Dec 2012

@author: Jamie
'''
# Contents of configuration file: twitter.cfg
#
# [DEFAULT]
# consumer_key = *********************
# consumer_secret = *******************************************
# access_token_key = **************************************************
# access_token_secret = ******************************************

import twitter
import ConfigParser

config = ConfigParser.RawConfigParser()

try:
    config.readfp(open('twitter.cfg'))
except IOError as e:
    print "I/O error ({0}): ({1})".format(e.errno, e.strerror)
    exit(1)
try:
    myConsumerKey = config.get('DEFAULT', 'consumer_key')
    myConsumerSecret = config.get('DEFAULT', 'consumer_secret')
    myAccessTokenKey = config.get('DEFAULT', 'access_token_key')
    myAccessTokenSecret = config.get('DEFAULT', 'access_token_secret')
except ConfigParser.NoSectionError as e:
    print "ConfigParser ({0})".format(e)
    exit(1)
except ConfigParser.NoOptionError as e:
    print "ConfigParser ({0})".format(e)
    exit(1)

client = twitter.Api(consumer_key=myConsumerKey,
                  consumer_secret=myConsumerSecret,
                  access_token_key=myAccessTokenKey,
                  access_token_secret=myAccessTokenSecret)

try:
    update = client.PostUpdate('The Twitter API is easy')
except twitter.TwitterError as e:
    print "TwitterError ({0})".format(e)
    exit(1)

print update.text