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
    fr = OrderedDict()
    start = OrderedDict()
    # start[fst1.keys()[0] + ',' + fst2.keys()[0]] = OrderedDict('')

    f1_keys = fst1.keys()
    f2_keys = fst2.keys()

    for n in range(len(fst1)):

        q1 = fst1[f1_keys[n]]
        q2 = fst2[f2_keys[n]]
        comp = f1_keys[n] + ',' + f2_keys[n]

        for m in range(len(q1)):
            t1 = q1.items()[m]
            t2 = q2.items()[m]

            trans1 = t1[0]
            trans2 = t2[0]

            if trans1.split('/')[1] == trans2.split('/')[0]:
                fr[comp] = OrderedDict()
                fr[comp][(trans1.split('/')[1] + '/' + trans2.split('/')[0])] = (
                    t1[1] + ',' + t2[1])

    return fr


def reconstructUpper(l, fst):
    for q in fst:
        trans = fst[q].keys()
        chars = [t.split('/') for t in trans]
        upper = [c[0] for c in chars]
        lower = [c[1] for c in chars]

        for i in range(len(lower)):
            if l == lower[i]:
                print upper[i]


def reconstructLower(u, fst):
    for q in fst:
        trans = fst[q].keys()
        chars = [t.split('/') for t in trans]
        upper = [c[0] for c in chars]
        lower = [c[1] for c in chars]

        for i in range(len(upper)):
            if u == upper[i]:
                print lower[i]


if __name__ == '__main__':
    f = readFST('test1.fst')
    f2 = readFST('test2.fst')

    fr = composeFST(f, f2)
    pass
