import os
import sys

# get relevant command line arguments
import collections

import math

args = sys.argv[1:]

# check if enough args given
if len(sys.argv) < 4:
    print 'usage: python tcomp1.py filename n file1name file2name ...'


def ngramify(file, n):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__), file))
    ngram = []
    with open(__location__) as f:
        lines = f.read().split()
        for line in lines:
            line = line.strip()
            ngram += list(zip(*[line[i:] for i in range(n)]))
    return ngram


def sim(ngram1, ngram2):
    freq1 = collections.Counter(ngram1)
    freq2 = collections.Counter(ngram2)

    for f in freq1:
        freq1[f] = float(freq1[f]) / len(ngram1)

    for f in freq2:
        freq2[f] = float(freq2[f]) / len(ngram2)

    diff = {}

    for f in freq1:
        if f in freq2:
            diff[f] = abs(freq1[f] - freq2[f])

    diff_sum = sum(diff.values())

    return round(1.0 - (diff_sum / 2), 3) if diff_sum else 0.0


if __name__ == '__main__':
    master_file = args[0]
    n = int(args[1])
    file_list = args[2:]

    ngram_master = ngramify(master_file, n)
    for file in file_list:
        ngram_file = ngramify(file, n)
        print 'Sim("', master_file, '","', file, '")=', sim(ngram_master, ngram_file)
