#!/usr/bin/env python
from sys import stdin, argv

def TranscribeDNA(sequence=None):
    """
    Given test:
    >>> seq = 'GATGGAACTTGACTACGTAAATT'
    >>> TranscribeDNA(seq)
    GAUGGAACUUGACUACGUAAAUU
    """
    if not sequence:
        sequence = stdin.next().upper()
    sequence = sequence.replace('T', 'U')
    print sequence

if __name__ == '__main__':
    if len(argv) == 2:
        # something like 'python file.py test'
        import doctest
        doctest.testmod()
    else:
        TranscribeDNA()
