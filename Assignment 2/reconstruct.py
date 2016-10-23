import os

import sys
from collections import OrderedDict

import itertools

args = sys.argv[1:]

# check if enough args given
if len(args) < 3:
    print 'usage: python reconstruct.py surface/lexical wlf F1 ... Fn'
    sys.exit(1)


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

    f1_keys = fst1.keys()
    f2_keys = fst2.keys()

    for n in range(min(len(fst1), len(fst2))):

        q1 = fst1[f1_keys[n]]
        q2 = fst2[f2_keys[n]]
        comp = f1_keys[n] + ',' + f2_keys[n]

        for m in range(len(q1)):
            t1 = q1.items()[m]
            t2 = q2.items()[m]

            trans1 = t1[0]
            trans2 = t2[0]

            if trans1.split('/')[1] == trans2.split('/')[0]:

                if comp not in fr:
                    fr[comp] = OrderedDict()
                fr[comp][(trans1.split('/')[1] + '/' + trans2.split('/')[0])] = t1[1] + ',' \
                                                                                        '' + t2[1]

    return fr


def reconstructUpper(l, fst):
    for q in fst:
        trans = fst[q].keys()
        chars = [t.split('/') for t in trans]
        upper = [c[0] for c in chars]
        lower = [c[1] for c in chars]

        for ch in l:
            for i in range(len(lower)):
                if ch == lower[i] or (lower[i] == '-' or ch == '-'):
                    if q[2] == 'F':
                        sys.stdout.write(upper[i])


def reconstructLower(u, fst):
    for q in fst:
        trans = fst[q].keys()
        chars = [t.split('/') for t in trans]
        upper = [c[0] for c in chars]
        lower = [c[1] for c in chars]

        for ch in u:
            for i in range(len(upper)):
                if ch == upper[i] or (upper[i] == '-' or ch == '-'):
                    if q[2] == 'F':
                        sys.stdout.write(lower[i])


if __name__ == '__main__':
    sur_low = args[0]

    if sur_low != 'surface' and sur_low != 'lexical':
        print 'Must specify if reconstruction is surface or lexical.'
        sys.exit(1)

    wlsf = args[1]
    file_list = args[2:]

    fsts = []

    for f in file_list:
        __path__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__), f))
        fsts.append(readFST(__path__))

    fst = fsts[0]

    for i in range(1, len(fsts)):
        fst = composeFST(fst, fsts[i])

    num_trans = 0
    for s in fst:
        num_trans += len(fst[s].keys())
    print "Composed FST has " + str(len(fst.keys())) + " states and " + str(num_trans) + \
          " transitions.\n"

    __path__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__), wlsf))

    with open(__path__) as wf:
        for line in wf.readlines():
            line = line.strip()
            print "Reconstructing " + sur_low + " form for " + line + ":"
            sys.stdout.write('\t')
            for ch in line:
                if sur_low == 'surface':
                    reconstructUpper(ch, fst)
                else:
                    reconstructLower(ch, fst)
            print '\n'
