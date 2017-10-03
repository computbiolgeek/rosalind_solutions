#!/usr/bin/env python3

import sys


def hamming_distance(s1, s2):
    '''
    Compute the Hamming distance between two strings.
    '''
    assert len(s1) == len(s2)
    
    dist = 0
    for a, b in zip(s1, s2):
        if a != b:
            dist += 1
    return dist


def main():
    '''
    '''
    args = sys.argv

    # if -h is given, print help
    if '-h' in args:
        print('usage: count_snps.py <input file>')
        sys.exit(0)

    # read in file
    with open(args[1], 'rt') as f:
        lines = [l.strip() for l in f.readlines()]

    # print the Hamming distance between the two strings
    print('Hamming distance:', hamming_distance(lines[0], lines[1]))


if __name__ == '__main__':
    main()
