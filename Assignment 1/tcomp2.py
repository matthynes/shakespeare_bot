#########################################################
##  CS 4750 (Fall 2016), Assignment #1, Question #2    ##
##   Script File Name: tcomp2.py                       ##
##       Student Name: Matthew Hynes                   ##
##         Login Name: mrh830                          ##
##              MUN #: 201200318                       ##
#########################################################

"""
This program calculates the similarity between two or more text files based on the formula:
Sim(X, Y) = 1.0 - (SD(X, Y) / (nW(X) + nW(Y))), where nW(X) and nW(Y) are the numbers of words that
occur in X and Y and SD(X, Y) is the total number of words that occur uniquely in X or Y.

It accepts, as command line arguments, a master text file and one or more additional
text files. It will then output the similarity of each additional as compared to the master text
file and finally state which file is most similar to it.
"""

import os
import sys

args = sys.argv[1:]

# check if enough args given
if len(args) < 2:
    print 'usage: python tcomp2.py filename filename1 filename2 ...'


def nw(file):
    __path__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__), file))

    # read file and return a list of unique words
    with open(__path__, 'r') as f:
        lines = f.read().split()
        return set(lines)


def sd(nw1, nw2):
    set1 = set(nw1).difference(nw2)
    set2 = set(nw2).difference(nw1)

    return len(set1) + len(set2)


def sim(file1, file2):
    nw1 = nw(file1)
    nw2 = nw(file2)

    sd_comp = sd(nw1, nw2)
    return 1.0 - (float(sd_comp) / (len(nw1) + len(nw2)))


if __name__ == '__main__':
    master_file = args[0]
    file_list = args[1:]

    sims = {}

    for file in file_list:
        result = round(sim(master_file, file), 3)
        print 'Sim("{0}","{1}")={2}'.format(master_file, file, result)
        sims[file] = result

    print "{0} is most similar to {1}".format(max(sims.iterkeys(), key=lambda x: sims[x]),
                                              master_file)
