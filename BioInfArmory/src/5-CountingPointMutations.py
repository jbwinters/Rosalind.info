#!/usr/bin/env python
from sys import stdin, argv

def count_point_mutations(sequences=None):
    r"""
    Given test:
    >>> seqs = '''GAGCCTACTAACGGGAT
    ... CATCGTAATGACGGCCT'''
    >>> count_point_mutations(seqs)
    7
    """
    if not sequences:
        sequences = stdin.read()
    sequences = sequences.split('\n')

    differences = sum(n1 != n2 for n1, n2 in zip(sequences[0], sequences[1]))
    print differences

if __name__ == '__main__':
    if len(argv) == 2:
        # something like 'python file.py test'
        import doctest
        doctest.testmod()
    else:
        count_point_mutations()
