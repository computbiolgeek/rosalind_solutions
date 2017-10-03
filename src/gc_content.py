#!/usr/bin/env python3

import sys

def compute_gc_content(string):
    '''
    Compute the GC content of the given string.
    '''
    gc_count = string.count('G') + string.count('C')
    return gc_count / len(string)


def read_fasta(fastafile):
    '''
    Parse a fasta file into a list of dicts, each dict is a 
    '''
    seqs = []
    with open(fastafile, 'rt') as f:
        # get the first line
        first_line = next(f)
        if not first_line.startswith('>'):
            print('Invalid fasta file, first line must start with \'>\'.')
            sys.exit(0)
        seq_id = first_line.strip().lstrip('>')

        # read the remaining lines
        seq = ''
        for line in f:
            # skip empty lines
            if not line.strip():
                continue
            if line.startswith('>'):
                # append the previous sequence to the list
                seqs.append((seq_id, seq))
                # found a new sequence record
                seq_id = line.strip().lstrip('>')
                seq = ''
            else:
                # concatenate sequence lines
                seq += line.strip()
    return seqs


def main():
    '''
    Call helper functions to compute GC contents.

    '''
    args = sys.argv

    # if -h is given on the command line, print the help information
    if '-h' in args:
        print('usage: gc_content.py -f <fasta file> -o <output file>')
        sys.exit(0)

    # read in fasta file
    seqs = read_fasta(args[2])

    # compute GC content
    gc_content = {s[0]: compute_gc_content(s[1]) for s in seqs}

    # print results
    with open(args[4], 'wt') as f:
        for key, value in gc_content.items():
            print('%s: %.6f' % (key, value), file=f)


if __name__ == '__main__':
    main()
