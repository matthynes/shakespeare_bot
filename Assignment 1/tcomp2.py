import os
import sys

args = sys.argv[1:]


def nw(file):
    __path__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__), file))

    with open(__path__, 'r') as f:
        lines = f.read().split()
        return set(lines)


def sd(nw1, nw2):
    set1 = set(nw1).difference(nw2)
    set2 = set(nw2).difference(nw1)

    return len(set1) + len(set2)


def sim(file1, file2):
    nw1 = nw(file1)
    nw2 = nw(file2)

    sd_comp = sd(nw1, nw2)
    return 1.0 - (float(sd_comp) / (len(nw1) + len(nw2)))


if __name__ == '__main__':
    master_file = args[0]
    file_list = args[1:]

    sims = {}

    for file in file_list:
        result = round(sim(master_file, file), 3)
        #    print 'Sim("', master_file, '","', file, '")=', result
        print 'Sim("{0}","{1}")={2}'.format(master_file, file, result)
        sims[file] = result

    print "{0} is most similar to {1}".format(max(sims.iterkeys(), key=lambda x: sims[x]),
                                              master_file)
