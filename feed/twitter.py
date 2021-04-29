import tweepy
import sys
import json
from utilities.load_file import LoadFile
from abc import ABC, abstractmethod

# Tweepy supports both OAuth 1a (application-user) and OAuth 2 (application-only) authentication.
CONFIG = LoadFile().load_config()
STORE_PATH = LoadFile("data", "tweet.json").path_str()

# Authentication
KEY = CONFIG["Tweeter"]["tweet_api_key"]
SECRET = CONFIG["Tweeter"]["tweet_api_secret_key"]
A_TOKEN = CONFIG["Tweeter"]["tweet_access_token"]
A_TOKEN_SECRET = CONFIG["Tweeter"]["tweet_access_token_secret"]

# Set OAuth 1a credentials
AUTH = tweepy.OAuthHandler(KEY,SECRET)
AUTH.set_access_token(A_TOKEN,A_TOKEN_SECRET)

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api = None):
        super().__init__()
        self.num_tweets = 0
        self.tweet_list = []
        self.file = open(STORE_PATH,"w")
    def on_status(self,status):
        tweet=status._json
        self.file.write(json.dumps(tweet) + '\n')
        self.num_tweets += 1
        if self.num_tweets < 1000:
            return True
        else:
            return False
        
        self.file.close()
        
# Create streaming object and authenticate
agent = MyStreamListener()
stream = tweepy.Stream(AUTH,agent)
# To capture the data by keywords
stream.filter(track=['bitcoin', 'btc', 'cryptocurrency'])