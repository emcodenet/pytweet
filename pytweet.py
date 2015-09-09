import random
from random import randint
import sys
import time
from termcolor import colored, cprint
import tweepy
from tweepy import StreamListener
from tweepy import Stream
import json

CONSUMER_KEY = 'xxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxx'
ACCESS_KEY = 'xxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

colors = ['grey','red','green','yellow','blue','magenta','cyan','white']

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):

    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print ( colored( '%s' % (decoded['text'].encode('ascii', 'ignore'))  , colors[randint(0,7)] ) )
        print ('')
	time.sleep(2)
        return True

    def on_error(self, status):
        print (colored( status, colors[randint(0,7)] ) )

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    stream = tweepy.Stream(auth, l)
    stream.filter(track=['programming', 'batman'])

#streamer core code borrowed from http://code.runnable.com/Us9rrMiTWf9bAAW3/how-to-stream-data-from-twitter-with-tweepy-for-python