'''
Created on 3 Dec 2012

@author: Jamie
'''

import twitter
import json
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


creds = client.VerifyCredentials()

decoded = json.loads(str(creds))

#print decoded['name']

#for key in decoded:
#    print "{0}: {1}".format(key, decoded[key])

#print"--------------"

def decode_json(json_string):
    print "----------------------------------------"
    print "json:  " + json_string
    content = json.loads(str(json_string))
    for key, value in content.iteritems():
        print "========================="
        print key
        if type(value) == type({}):
            strg = str(json.dumps(value))
            decode_json(strg)
        else:
            print value
        

decode_json(str(creds))



