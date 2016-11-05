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

    grammar = collections.defaultdict(str)

    with open(__path__, 'r') as cf:
        for line in cf.readlines():
            rhs, lhs = line.strip().split(' -> ')
            grammar[rhs] = lhs
    

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
