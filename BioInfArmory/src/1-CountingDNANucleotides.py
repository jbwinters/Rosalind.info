#!/usr/bin/env python

from sys import stdin, argv
from collections import Counter

def count_dna_nucleotides(sequence=None):
    """
    Given test:
    >>> seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    >>> count_dna_nucleotides(seq)
    20 12 17 21
    """
    if not sequence:
        sequence = stdin.next().upper()
    counts = Counter(sequence)
    print counts['A'], counts['C'], counts['G'], counts['T']

if __name__ == '__main__':
    if len(argv) == 2:
        # something like 'python file.py test'
        import doctest
        doctest.testmod()
    else:
        count_dna_nucleotides()
