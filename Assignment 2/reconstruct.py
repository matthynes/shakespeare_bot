import os

import sys
from collections import defaultdict


def readFST(filename):
    name, ext = os.path.splitext(filename)

    if not ext == '.fst':
        print('Files must be .fst type.')

    fst = defaultdict(lambda: defaultdict(str))

    with open(filename, 'r') as file:
        lines = file.readlines()
        for n in range(1, len(lines)):
            line = lines[n].strip('\n')
            if line[0].isdigit():
                fst[line] = {}

                for m in range(n+1, len(lines)):
                    l = lines[m].strip('\n')
                    if not l[0].isdigit():
                        upper_lower = l[2] + '/' + l[4]
                        fst[line][upper_lower] = l[6]
                    else:
                        break
        pass


if __name__ == '__main__':
    readFST(sys.argv[1])
