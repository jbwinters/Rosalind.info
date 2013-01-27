#!/usr/bin/env python
from sys import stdin, argv
import re

def find_all_occurrences_of_motif(sequences=None):
    r"""
    Given test:
    >>> seqs = '''GATATATGCATATACTT
    ... ATAT'''
    >>> find_all_occurrences_of_motif(seqs)
    2 4 10
    """
    if not sequences:
        sequences = stdin.read()
    sequence, motif = sequences.strip().split('\n')
    re_motif = '(?=%s)' % motif
    locations = (match.start() for match in re.finditer(re_motif, sequence))
    print ' '.join(str(x + 1) for x in locations)

if __name__ == '__main__':
    if len(argv) == 2:
        # something like 'python file.py test'
        import doctest
        doctest.testmod()
    else:
        find_all_occurrences_of_motif()
