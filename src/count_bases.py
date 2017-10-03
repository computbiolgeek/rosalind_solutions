#!/usr/bin/env python3

import sys

def main():
    '''
    Count the respective number of times each nucleotide occurs in the DNA sequence.
    '''
    args = sys.argv

    # if -h is given on the command line, print the help message
    if '-h' in args:
        print('usage: count_bases.py <dna file>')
        sys.exit(0)

    # read in the DNA sequence
    with open(args[1], 'rt') as f:
        dna = ''.join(l.strip() for l in f.readlines())

    # count nucleotide occurrences
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for n in dna:
        if n in 'ACGT':
            counts[n] += 1

    # print the output
    for key, value in counts.items():
        print('%s: %d' % (key, value))


if __name__ == '__main__':
    main()
