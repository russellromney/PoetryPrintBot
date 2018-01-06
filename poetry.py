import tweepy
import time

# my private credentials
from poetry_credentials import *


poem = 'annabelle_lee.txt'

# authorize the API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# grab lines from the text file
filename=open(argfile,'r')
f=filename.readlines()
filename.close()

# do the printing
for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes
