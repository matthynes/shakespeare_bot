import os

import tweepy
import markovify

from settings import CONSUMER_SECRET, CONSUMER_KEY, ACCESS_TOKEN_SECRET, ACCESS_TOKEN

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

with open(os.path.dirname(__file__) + '/corpus.txt', 'r') as corpus:
    model = markovify.Text(corpus.read())

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
