#!/usr/bin/env python
from __future__ import division
from sys import stdin, argv

def mendels_first_law(probabilities=None):
    """
    Given test:
    >>> mendels_first_law('2 2 2')
    0.78333
    """
    if not probabilities:
        probabilities = stdin.read()
    K, M, N = [int(x) for x in probabilities.split()]
    # K: homozygous dominant
    # M: heterozygous
    # N: homozygous recessive
    tot_inds = K + M + N

    # probability calculation slightly expanded for clarity
    dominant_allele_probability = 1 - (N/tot_inds * (N-1)/(tot_inds-1)
                                    + N/tot_inds * M/(tot_inds-1) * 1/2 * 2
                                    + M/tot_inds * (M-1)/(tot_inds-1) * 1/4)
    return round(dominant_allele_probability, 5)



if __name__ == '__main__':
    if len(argv) == 2:
        # something like 'python file.py test'
        import doctest
        doctest.testmod()
    else:
        print mendels_first_law()
