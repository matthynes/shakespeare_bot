#########################################################
##  CS 4750 (Fall 2016), Assignment #3                 ##
##   Script File Name: CKYdet.py                       ##
##       Student Name: Matthew Hynes                   ##
##         Login Name: mrh830                          ##
##              MUN #: 201200318                       ##
#########################################################

"""
This program takes an eCNF-form grammar and a file with one or more utterances to parse (one
utterance per line) and outputs the corresponding parse tree associated with each utterance,
if one exists.
"""

import collections
import os
import sys

args = sys.argv[1:]

# check if enough args given
if len(args) != 2:
    print 'usage: python CKYdet.py eCNF_file utterance_file'


def cky_parse(ckyf, uttf):
    __path__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__), ckyf))

    grammar = collections.defaultdict(list)

    with open(__path__, 'r') as cf:
        # read in grammar and parse rules into LHS and RHS
        for line in cf.readlines():
            lhs, rhs = line.strip().split(' -> ')
            grammar[lhs].append(rhs)

    # anonymous function to return a rule, if one exists, given the matching rhs resolution to
    # said rule
    def get_rule(rhs):
        for r in rhs.split():
            for k, v in grammar.iteritems():
                if r in v:
                    return k
            return ''

    __path__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__), uttf))

    with open(__path__, 'r') as uf:
        lines = uf.readlines()

    for line in lines:
        line = line.strip().split()
        # get number of words (n)
        n = len(line)
        # initialize matrix/table
        matrix = [[None for _ in range(n + 1)] for _ in range(n + 1)]

        for j in range(n):
            for k in range(n + 1):
                matrix[j][k] = []
        # fill bottom diagonal with each word in the utterance
        for j in range(1, n + 1):
            matrix[j - 1][j] = '"' + line[j - 1] + '"'

        # fill in rest of table
        for i in range(1, n + 1):
            for j in range(i - 2, -1, -1):
                for k in range(j + 1, i):
                    if matrix[j][k] and matrix[k][i]:
                        rhs = matrix[j][k] + ' ' + matrix[k][i]
                        lhs = get_rule(rhs)
                        if lhs:
                            matrix[j][i] = lhs

        # trim excess rows
        matrix = matrix[:len(matrix) - 1]
        # check if solution (S) found and print the matrix
        if matrix[0][n]:
            for row in matrix:
                print row[1:]
        else:
            print 'No valid parse.'

        print ''


if __name__ == '__main__':
    ckyfile = args[0]
    uttfile = args[1]

    # check if file types are valid
    name, ext = os.path.splitext(ckyfile)
    if not ext == '.ecfg':
        print 'Grammar file must be of .ecfg type.'
        sys.exit(1)

    name, ext = os.path.splitext(uttfile)
    if not ext == '.utt':
        print 'Utterance file must be of .utt type.'
        sys.exit(1)

    cky_parse(ckyfile, uttfile)
