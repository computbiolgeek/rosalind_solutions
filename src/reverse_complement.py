#!/usr/bin/env python3

import sys

def reverse_complement(dna):
    '''
    Returns the reverse complement of a given DNA sequence.
    '''
    base_pairs = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([base_pairs[b] for b in dna[::-1]])


def split_input(string, chunk_size):
    '''
    Split a string into chunks, each chunk has chunk_size characters except the last chunk.

    '''
    chunks = len(string) // chunk_size
    output = []
    for i in range(0, chunks):
        output.append(string[chunk_size*i:chunk_size*(i+1)])
    output.append(string[chunk_size*chunks:])
    return '\n'.join(output)


def main():
    '''
    Given a DNA sequence, compute its reverse complement.    
    '''
    args = sys.argv;

    # if -h is given, print the help information
    if '-h' in args:
        print('usage: reverse_complement.py -i <dna file> -o <output file>')
        sys.exit(0)

    # read in the DNA sequence
    with open(args[2], 'rt') as f:
        dna = ''.join([l.strip() for l in f.readlines()])

    # compute the reverse complement
    dna_rc = reverse_complement(dna)

    # write out to file
    output = split_input(dna_rc, 60)
    with open(args[4], 'wt') as f:
        f.write(output)


if __name__ == '__main__':
    main()
