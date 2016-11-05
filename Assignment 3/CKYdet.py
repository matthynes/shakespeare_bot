import collections
import os
import sys

args = sys.argv[1:]

# check if enough args given
if len(args) != 2:
    print 'usage: python CKYdet.py eCNF_file utterance_file'

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
