import random
from random import randint
import sys
import time
from termcolor import colored, cprint
import tweepy

# get you keys when you make an app on https://apps.twitter.com/
CONSUMER_KEY = 'xxx'
CONSUMER_SECRET = 'xxx'
ACCESS_KEY = 'xxx'
ACCESS_SECRET = 'xxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

stuff = api.user_timeline(screen_name = 'twitter-username-to-get-tweets-from', count = 14000, include_rts = True)

colors = ['grey','red','green','yellow','blue','magenta','cyan','white']


for tweet in stuff:
	sys.stdout.write( colored( tweet.text + ' ' , colors[randint(0,7)] )  ),
    	sys.stdout.flush()
	time.sleep(1)

