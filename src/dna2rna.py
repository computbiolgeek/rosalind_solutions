#!/usr/bin/env python3

import sys

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
    Converts a coding DNA sequence to its transcribed mRNA sequence.
    '''
    args = sys.argv;

    # if -h is given, print help information
    if '-h' in args:
        print('usage: dna2rna.py -d <dna file> -r <rna file>')
        sys.exit(0)

    # read in DNA sequence
    with open(args[2], 'rt') as f:
        dna = ''.join([l.strip() for l in f.readlines()])

    # transcribe the DNA sequence to mRNA sequence
    rna = dna.replace('T', 'U')
    
    # write mRNA sequence to lines, each with a given number of bases
    chunk_size = 60
    rna_chunks = split_input(rna, chunk_size)

    # write out to file of the mRNA sequence
    with open(args[4], 'wt') as f:
        f.write(rna_chunks)


if __name__ == '__main__':
    main()
