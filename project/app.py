import os
import string
import time
import tweepy
import markovify
import editdistance
import pronouncing

from flask import Flask

from settings import CONSUMER_SECRET, CONSUMER_KEY, ACCESS_TOKEN_SECRET, ACCESS_TOKEN

app = Flask(__name__)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

STATE_SIZE = 3
NUM_TWEETS = 24
TWEET_INTERVAL = 60 * 60  # 60 * n = n-minute intervals

with open(os.path.dirname(os.path.abspath(__file__)) + '/corpus.txt', 'r') as corpus:
    model = markovify.Text(corpus.read(), state_size=STATE_SIZE)

public_tweets = api.user_timeline(count=NUM_TWEETS)


def generate_post():
    post = model.make_short_sentence(140)
    if post not in public_tweets:
        return post
    else:
        generate_post()


def make_post(post):
    api.update_status(post)
    print(post)


def is_iambic_pentameter(phrase):
    phrase = "".join(c for c in phrase if c not in string.punctuation).lower()
    phones = [pronouncing.phones_for_word(p) for p in phrase.split()]

    stresses = []

    for w in phones:
        stresses += pronouncing.stresses(w[0]) if w else '0'
    s = ''.join(stresses)
    dist = editdistance.eval(s, '0101010101')
    sim = round(((len(s) - dist) / len(s)) * 100)

    return sim >= 70.0


def main():
    while True:
        post = generate_post()
        if post:
            if is_iambic_pentameter(post):
                make_post(post)
                time.sleep(TWEET_INTERVAL)


main()
