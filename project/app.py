# import os
# import random
# import time
# import tweepy
# import markovify
#
# from settings import CONSUMER_SECRET, CONSUMER_KEY, ACCESS_TOKEN_SECRET, ACCESS_TOKEN
#
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#
# api = tweepy.API(auth)
#
# state_size = random.randrange(2, 5)
# TWEET_INTERVAL = 60 * 60  # 60 * n = n-minute intervals
#
# with open(os.path.dirname(__file__) + '/corpus.txt', 'r') as corpus:
#     model = markovify.Text(corpus.read(), state_size=state_size)
#
# public_tweets = api.user_timeline(count=24)
#
#
# def make_post():
#     for i in range(5):
#         post = model.make_short_sentence(140)
#
#         if post not in public_tweets:
#             # api.update_status(post)
#             print(state_size, post)
#
#
# if __name__ == '__main__':
#     while True:
#         make_post()
#         time.sleep(TWEET_INTERVAL)
import string

# from nltk.corpus import cmudict
#
# d = cmudict.dict()
import editdistance
import pronouncing

stresses = []

# def nsyl(w_word):
#     print(d[word.lower()])
#     for w in d[w_word.lower()]:
#         for c in w:
#             if c[-1] == str(1):
#                 stresses.append(1)
#             else:
#                 stresses.append(0)
#     return [len(list(y for y in x if y[-1].isdigit())) for x in d[w_word.lower()]]
#
#
# def stress(pron):
#     return [char for phone in pron for char in phone if char.isdigit()]


sums = 0
# for word in 'But, soft! what light through yonder window breaks?'.split():
#     word = "".join(c for c in word if c not in string.punctuation)
#     # w = d[word.lower()]
#     # print(w, word.lower())
#     # print(stress(d[word.lower()]))
#     # ns = nsyl(word)
#     # print(ns)
#     # stresses.append(ns)
#     # sum += ns[0]
#     # print(stresses)
#     phones = pronouncing.phones_for_word(word)
#     if not phones:
#         phones = ['0']
#     print(pronouncing.stresses(phones[0]))

phones = [pronouncing.phones_for_word(p)[0] for p in
          'now is the winter of our discontent'.split()]
total = sum([pronouncing.syllable_count(p) for p in phones])
print('Syllables: ', total)

for w in phones:
    stresses += pronouncing.stresses(w)
s = ''.join(stresses)
dist = editdistance.eval(s, '0101010101')
print(s)
print('0101010101')
print('Similarity: ', ((len(s) - dist) / 10) * 100, '%')
