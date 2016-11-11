import collections
import os
import sys

args = sys.argv[1:]

# check if enough args given
if len(args) != 2:
    print 'usage: python CKYdet.py eCNF_file utterance_file'


def CKYparse(ckyf, uttf):
    __path__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__), ckyf))

    grammar = collections.defaultdict(list)

    with open(__path__, 'r') as cf:
        for line in cf.readlines():
            lhs, rhs = line.strip().split(' -> ')
            grammar[lhs].append(rhs)

    __path__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__), uttf))

    with open(__path__, 'r') as uf:
        lines = uf.readlines()

    for line in lines:
        line = line.strip()
        n = len(line.split())
        matrix = [[None for x in range(n + 1)] for y in range(n + 1)]

        for j in range(1, n):
            for k in range(j - 1, 0, -1):
                for nt in grammar.keys():
                    print nt
                    matrix[j][k] = []


if __name__ == '__main__':
    ckyfile = args[0]
    uttfile = args[1]

    name, ext = os.path.splitext(ckyfile)
    if not ext == '.ecfg':
        print 'Grammar file must be of .ecfg type.'
        sys.exit(1)

    name, ext = os.path.splitext(uttfile)
    if not ext == '.utt':
        print 'Utterance file must be of .utt type.'
        sys.exit(1)

    CKYparse(ckyfile, uttfile)
