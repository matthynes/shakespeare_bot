#Shakespeare Bot

A Twitter bot that uses Markov chains to generate phrases in (mostly) iambic pentameter. The corpus itself is based on The Complete Works of William Shakespeare. Essentially it creates new, semi-intelligible, Shakespeare-esque tweets.

You can see it action [on Twitter](https://twitter.com/bardbot9000).

Running the bot is simple:

You will need to have Python 3.3+ installed.

  1. Download or clone the repository
  2. run `pip install -r requirements.txt`, you can create a vritualenv first if you wish
  3. Create a file called settings.py and fill it in with your oauth tokens provided by Twitter
  4. In a terminal, run `python app.py`
  
That's it! The bot should now automatically tweet every n minutes (15 by default). All the relevant settings such as `TWEET_INTERVAL` and `STATE_SIZE` are at the top of the file, you may change them as you wish.

This project makes use of the following fantastic libraries (in no particular order):

  * [marovify](https://github.com/jsvine/markovify)
  * [Tweepy](https://github.com/tweepy/tweepy)
  * [pronouncingpy](https://github.com/aparrish/pronouncingpy)
  * [Natural Language Toolkit](http://www.nltk.org/)
  * [editdistance](https://github.com/aflc/editdistance)
  
The Complete Works of William Shakespeare is provided by Project Gutenberg at http://www.gutenberg.org/ebooks/100.
