#!/usr/bin/env python
from sys import stdin, argv

def complement_dna(sequence=None):
    """
    Given test:
    >>> seq = 'AAAACCCGGT'
    >>> complement_dna(seq)
    'ACCGGGTTTT'
    """
    if not sequence:
        sequence = stdin.next().upper()
    complement = sequence.replace('A', 't').\
                        replace('T','a').\
                        replace('C','g').\
                        replace('G','c').\
                        upper()[::-1]
    return complement

if __name__ == '__main__':
    if len(argv) == 2:
        # something like 'python file.py test'
        import doctest
        doctest.testmod()
    else:
        print complement_dna()
