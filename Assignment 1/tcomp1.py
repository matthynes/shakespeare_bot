#########################################################
##  CS 4750 (Fall 2016), Assignment #1, Question #1    ##
##   Script File Name: tcomp1.py                       ##
##       Student Name: Matthew Hynes                   ##
##         Login Name: mrh830                          ##
##              MUN #: 201200318                       ##
#########################################################

"""
This program calculates the n-gram similarity between two or more text files.
It accepts, as command line arguments, a master text file, an number n, and one or more additional
text files.
It will then output the similarity of each additional as compared to the master text file and
finally state which file is most similar to it.
"""

import collections
import os
import sys

args = sys.argv[1:]

# check if enough args given
if len(args) < 3:
    print 'usage: python tcomp1.py filename n filename1 filename2 ...'


def ngramify(file, n):
    # relative base path
    __path__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__), file))
    ngram = []
    with open(__path__) as f:
        lines = f.read().split()
        for line in lines:
            # remove whitespaces
            line = line.strip()
            # extract up to n characters from line and zip them together into a tuple,
            # then progressively build a list of tuples
            ngram += list(zip(*[line[i:] for i in range(n)]))
    return ngram


def sim(ngram1, ngram2):
    # generate frequency diagrams for each n-gram
    freq1 = collections.Counter(ngram1)
    freq2 = collections.Counter(ngram2)

    for f in freq1:
        freq1[f] = float(freq1[f]) / len(ngram1)

    for f in freq2:
        freq2[f] = float(freq2[f]) / len(ngram2)

    diff = {}

    # get difference between each n-gram in intersection of freq1 & freq2
    for f in freq1:
        if f in freq2:
            diff[f] = abs(freq1[f] - freq2[f])
        else:
            diff[f] = freq1[f]

    # also include n-grams that appear only in freq2
    for f in freq2:
        if f not in freq1:
            diff[f] = freq2[f]

    diff_sum = sum(diff.values())

    return round(1.0 - (diff_sum / 2), 3) if diff_sum else 0.0


if __name__ == '__main__':
    master_file = args[0]
    n = int(args[1])
    file_list = args[2:]

    sims = {}

    ngram_master = ngramify(master_file, n)
    for file in file_list:
        ngram_file = ngramify(file, n)
        result = sim(ngram_master, ngram_file)
        print 'Sim("{0}","{1}")={2}'.format(master_file, file, result)
        sims[file] = result

    # get largest result from similarity dict which indicates file most similar to master file
    print "{0} is most similar to {1}".format(max(sims.iterkeys(), key=lambda x: sims[x]),
                                              master_file)
