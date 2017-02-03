Twitter Wrapper

Author - Jamie Jackson - http://blog.jacobean.net

History
-------

0.0.4	19 Dec 12	Handling general exception around PostUpdate()
0.0.3	15 Dec 12	Added instructions and comments.
0.0.2	14 Dec 12	Added exception handling.
0.0.1	09 Dec 12	Initial Release.

Introduction
------------

This class has the following functionality:

1.	Wraps the OAuth authentication within the class constructor.  By creating a configuration
file in the correct format, this is read & used to connect to twitter.

2.	One member function provides the user to post an update (or tweet) on twitter.

3.  That is all ... for now ...

Instructions
------------

Dependencies:

	OAuth2 Python module - http://pypi.python.org/pypi/oauth2/
	Twitter Python module - http://pypi.python.org/pypi/twitter/

Install the dependencies and this tweeter Python module in the usual way.

Register you application on the Twitter Developers site (https://dev.twitter.com/).Take
a note of the OAuth credentials provided by twitter.

Create a configuration file called, by default, tweeter.cfg, with the following:

	[DEFAULT]
	consumer_key = *********************
	consumer_secret = *******************************************
	access_token_key = **************************************************
	access_token_secret = ******************************************

Code example:

	from tweeter import tweeter
	
	myTweeter = tweeter()
	myTweeter.tweet("I Love Tweeter!")


