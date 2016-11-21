import os
import time
import tweepy
import markovify

from settings import CONSUMER_SECRET, CONSUMER_KEY, ACCESS_TOKEN_SECRET, ACCESS_TOKEN

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

STATE_SIZE = 2
TWEET_INTERVAL = 60 * 60  # 60 * n = n-minute intervals

with open(os.path.dirname(__file__) + '/corpus.txt', 'r') as corpus:
    model = markovify.Text(corpus.read(), state_size=STATE_SIZE)

public_tweets = api.user_timeline(count=24)


def make_post():
    post = model.make_short_sentence(140)

    if post not in public_tweets:
        api.update_status(post)


if __name__ == '__main__':
    while True:
        make_post()
        time.sleep(TWEET_INTERVAL)
