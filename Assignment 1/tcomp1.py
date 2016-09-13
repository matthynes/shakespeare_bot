import sys

# get relevant command line arguments
args = sys.argv[1:]

# check if enough args given
if len(sys.argv) < 4:
    print 'usage: python tcomp1.py filename n file1name file2name ...'


def sim(master_file, n, file_list):
    pass


if __name__ == '__main__':
    sim(args[0], args[1], args[2:])
