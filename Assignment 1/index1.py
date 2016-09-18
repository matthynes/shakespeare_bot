import os
import string
import sys
from collections import defaultdict

args = sys.argv[1:]

if __name__ == '__main__':
    word_file = args[0]
    text_file = args[1]
    index_file = args[2]

    ignored = []
    found = defaultdict(str)

    __base__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__base__, word_file), 'r') as w_f:
        for word in w_f.read().splitlines():
            if word.isalpha():
                ignored.append(word)

    with open(os.path.join(__base__, text_file), 'r') as t_f:
        for n, l in enumerate(t_f, 1):
            for w in l.split():
                w = w.translate(None, string.punctuation)
                if w not in ignored and w.isalpha():
                    found[w] += str(n) + ','

    with open(os.path.join(__base__, index_file), 'w') as i_f:
        for word in sorted(found):
            ln = found[word].split(',')
            i_f.write(word + ': ')
            for n in ln:
                i_f.write(n + ' ')
            i_f.write('\n')
