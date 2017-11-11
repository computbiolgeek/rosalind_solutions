#!/usr/bin/env python3

import sys


def rna2aa(rna):
    '''
    Parameters
    ----------
    rna : str
        A valid three-letter RNA string.

    Returns
    -------
        One-letter amino acid type.
    '''
    genetic_codes = {
        'UUU': 'F',
        'CUU': 'L',
        'AUU': 'I',
        'GUU': 'V',
        'UUC': 'F',
        'CUC': 'L',
        'AUC': 'I',
        'GUC': 'V',
        'UUA': 'L',
        'CUA': 'L',
        'AUA': 'I',
        'GUA': 'V',
        'UUG': 'L',
        'CUG': 'L',
        'AUG': 'M',
        'GUG': 'V',
        'UCU': 'S',
        'CCU': 'P',
        'ACU': 'T',
        'GCU': 'A',
        'UCC': 'S',
        'CCC': 'P',
        'ACC': 'T',
        'GCC': 'A',
        'UCA': 'S',
        'CCA': 'P',
        'ACA': 'T',
        'GCA': 'A',
        'UCG': 'S',
        'CCG': 'P',
        'ACG': 'T',
        'GCG': 'A',
        'UAU': 'Y',
        'CAU': 'H',
        'AAU': 'N',
        'GAU': 'D',
        'UAC': 'Y',
        'CAC': 'H',
        'AAC': 'N',
        'GAC': 'D',
        'UAA': 'Stop',
        'CAA': 'Q',
        'AAA': 'K',
        'GAA': 'E',
        'UAG': 'Stop',
        'CAG': 'Q',
        'AAG': 'K',
        'GAG': 'E',
        'UGU': 'C',
        'CGU': 'R',
        'AGU': 'S',
        'GGU': 'G',
        'UGC': 'C',
        'CGC': 'R',
        'AGC': 'S',
        'GGC': 'G',
        'UGA': 'Stop',
        'CGA': 'R',
        'AGA': 'R',
        'GGA': 'G',
        'UGG': 'W',
        'CGG': 'R',
        'AGG': 'R',
        'GGG': 'G'
    }
    return genetic_codes[rna.upper()]


def main():
    '''
    '''
    args = sys.argv

    if '-h' in args:
        print('usage: rna2prot.py <RNA sequence file>')
        sys.exit(0)

    if len(args) != 2:
        print('usage: rna2prot.py <RNA sequence file>')

    # parse the RNA sequence file
    with open(args[1], 'rt') as f:
        rna_sequence = ''.join([l.strip() for l in f.readlines() if not l.startswith(('>', '#'))])

    # check that the given RNA sequence is valid
    if len(rna_sequence) % 3:
        print('The length of the given RNA sequence is not a multiple of 3!')
        sys.exit(1)
    if set(rna_sequence) != {'A', 'G', 'C', 'U'}:
        print('The given RNA sequence has illegal base that is not one of A, G, C, or U!')
        sys.exit(1)

    # translate the RNA sequence into amino acid sequence
    prot_sequence = ''.join([rna2aa(rna_sequence[i:i+3]) for i in range(0, len(rna_sequence), 3)])

    # print the protein sequence
    print(prot_sequence)


if __name__ == '__main__':
    main()
