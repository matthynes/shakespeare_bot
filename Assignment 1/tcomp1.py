import os
import sys

# get relevant command line arguments
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
            line = list(line)
            ngram += list(zip(*[line[i:] for i in range(n)]))
    return ngram


def sim(ngram1, ngram2):
    pass


if __name__ == '__main__':
    master_file = args[0]
    n = args[1]
    file_list = args[2:]

    ngram_master = ngramify(master_file, n)
    for file in file_list:
        ngram_file = ngramify(file, n)
        print sim(ngram_master, ngram_file)
