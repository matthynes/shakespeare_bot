import os

import sys
from collections import OrderedDict


def readFST(filename):
    name, ext = os.path.splitext(filename)

    if not ext == '.fst':
        print('Files must be .fst type.')

    fst = OrderedDict()

    with open(filename, 'r') as file:
        lines = file.readlines()
        for n in range(1, len(lines)):
            line = lines[n].strip('\n')
            if line[0].isdigit():
                if line not in fst:
                    fst[line] = OrderedDict()

                for m in range(n + 1, len(lines)):
                    l = lines[m].strip('\n')
                    fl = fst[line]
                    if not l[0].isdigit():
                        upper_lower = l[2] + '/' + l[4]
                        fl[upper_lower] = l[6]
                    else:
                        break
    return fst


def composeFST(fst1, fst2):
    for q in fst1:
        pass


def reconstructUpper(l, fst):
    for q in fst:
        trans = fst[q].keys()
        chars = [t.split('/') for t in trans]
        upper = [c[0] for c in chars]

        print upper


def reconstructLower(l, fst):
    pass


if __name__ == '__main__':
    f = readFST(sys.argv[1])

    reconstructUpper('a', f)
