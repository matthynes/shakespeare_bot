#########################################################
##  CS 4750 (Fall 2016), Assignment #1, Question #3    ##
##   Script File Name: index1.py                       ##
##       Student Name: Matthew Hynes                   ##
##         Login Name: mrh830                          ##
##              MUN #: 201200318                       ##
#########################################################

"""
This program outputs any words in a given text document (and the line numbers on which they
occur) excluding words that are provided by another text file which specifies the words to be
ignored.

It accept, as command line arguments, an "ignored words" text file with each word to be ignored on
its own line, the text file document to be searched, and a file to which the resulting output
will be written.
"""

import os
import string
import sys
from collections import defaultdict

args = sys.argv[1:]

# check if enough args given
if len(args) != 3:
    print 'usage: python index1.py ignored_file text_file output_file'

if __name__ == '__main__':
    word_file = args[0]
    text_file = args[1]
    index_file = args[2]

    ignored = []
    found = defaultdict(str)

    __base__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__base__, word_file), 'r') as w_f:
        # iterate through ignored word list and add any actual words
        for word in w_f.read().splitlines():
            if word.isalpha():
                ignored.append(word)

    with open(os.path.join(__base__, text_file), 'r') as t_f:
        # iterate through text file, remove punctuation, and add any words (and their line
        # numbers) that aren't on the ignored words list
        for n, l in enumerate(t_f, 1):
            for w in l.split():
                w = w.translate(None, string.punctuation)
                if w not in ignored and w.isalpha():
                    found[w] += str(n) + ','

    with open(os.path.join(__base__, index_file), 'w') as i_f:
        for word in sorted(found):
            ln = found[word].split(',')
            i_f.write(word + ': ')
            for n in ln:
                i_f.write(n + ' ')
            i_f.write('\n')
