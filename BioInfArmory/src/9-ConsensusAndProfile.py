#!/usr/bin/env python
from sys import stdin, argv
from collections import Counter
import operator

def consensus_and_profile(sequences=None):
    r"""
    Given test:
    >>> seqs = '''ATCCAGCT
    ... GGGCAACT
    ... ATGGATCT
    ... AAGCAACC
    ... TTGGAACT
    ... ATGCCATT
    ... ATGGCACT'''
    >>> consensus_and_profile(seqs)
    ATGCAACT
    A: 5 1 0 0 5 5 0 0
    C: 0 0 1 4 2 0 6 1
    G: 1 1 6 3 0 1 0 0
    T: 1 5 0 0 0 1 1 6
    """
    if not sequences:
        sequences = stdin.read()
    sequences = sequences.strip().split()
    transposed = zip(*sequences)
    column_counts = [Counter(column) for column in transposed]
    def most_common_key (counts):
        return max(counts.iteritems(), key=operator.itemgetter(1))[0]
    most_likely_nucleotides = (most_common_key(counts)
                                for counts in column_counts)

    print ''.join(most_likely_nucleotides)
    def print_count_totals(nuc):
        print '%s:' % nuc, ' '.join(str(counts[nuc]) for counts in column_counts)
    print_count_totals('A')
    print_count_totals('C')
    print_count_totals('G')
    print_count_totals('T')

if __name__ == '__main__':
    if len(argv) == 2:
        # something like 'python file.py test'
        import doctest
        doctest.testmod()
    else:
        consensus_and_profile()
