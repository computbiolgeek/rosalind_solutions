#!/usr/bin/env python3

import sys


def main():
    '''
    '''
    args = sys.argv

    # if -h is given on the command line, print help information
    if '-h' in args:
        print('usage: dna_motif.py -d <dna file> -m <motif file>')
        sys.exit(0)

    # parse the DNA sequence
    with open(args[2], 'rt') as f:
        dna = ''.join([l.strip() for l in f.readlines()])

    # read in the motif
    with open(args[4], 'rt') as f:
        motif = ''.join([l.strip() for l in f.readlines()])

    # locate the motif in the DNA sequence
    for i, a in enumerate(dna):
        if a != motif[0]:
            continue
        else:
