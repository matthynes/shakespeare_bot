import os
import sys

# get relevant command line arguments
import collections

args = sys.argv[1:]

# check if enough args given
if len(sys.argv) < 4:
    print 'usage: python tcomp1.py filename n file1name file2name ...'


def ngramify(file, n):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__), file))
    ngram = []
    with open(__location__) as f:
        lines = f.read().splitlines()
        for line in lines:
            # line = list(line)
            ngram += list(zip(*[line[i:] for i in range(n)]))
    return ngram


def sim(ngram1, ngram2):
    # freq1 = collections.Counter(ngram1)
    # freq2 = collections.Counter(ngram2)
    #
    # ng1s = float(len(ngram1))
    # ng2s = float(len(ngram2))
    #
    # for f, n in freq1.items():
    #     freq1[f] = (n / ng1s)
    # for f, n in freq2.items():
    #     freq2[f] = (n / ng2s)
    # c = 0
    # for ff, nn in freq1.items():
    #     if ff in freq2:
    #         c += (nn + freq2[ff])
    #
    # return 1.0 - (c)
    ngset1 = set(ngram1)
    ngset2 = set(ngram2)

    common = ngset1.intersection(ngset2)
    all = ngset1.union(ngset2)

    if common:
        return round(len(common) / float(len(all)), 3)
    else:
        return 0.0


if __name__ == '__main__':
    master_file = args[0]
    n = int(args[1])
    file_list = args[2:]

    ngram_master = ngramify(master_file, n)
    for file in file_list:
        ngram_file = ngramify(file, n)
        print 'Sim("', master_file, '","', file, '")=', sim(ngram_master, ngram_file)
