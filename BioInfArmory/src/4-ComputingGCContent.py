#!/usr/bin/env python
from sys import stdin, argv
from utilities import FASTA_Dataset
from collections import Counter
from decimal import *

def gc_content(data):
    """
    >>> gc_content('ATGCC')
    60.0
    """
    counts = Counter(data.upper())
    AT_count = counts['A'] + counts['T']
    GC_count = counts['G'] + counts['C']

    return GC_count * 100. / (AT_count + GC_count)

def compute_max_gc_content(dataset=None):
    r"""
    Given test:
    >>> dataset = '''>Rosalind_6404
    ... CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
    ... TCCCACTAATAATTCTGAGG
    ... >Rosalind_5959
    ... CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
    ... ATATCCATTTGTCAGCAGACACGC
    ... >Rosalind_0808
    ... CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
    ... TGGGAACCTGCGGGCAGTAGGTGGAAT'''
    >>> compute_max_gc_content(dataset)
    Rosalind_0808
    60.91954
    """
    if not dataset:
        dataset = stdin.read()

    fasta_dataset = FASTA_Dataset(dataset)

    max_gc_content = float("-inf")
    max_gc_label = ''

    for data_label, data in fasta_dataset:
        record_gc_content = gc_content(data)
        if record_gc_content > max_gc_content:
            max_gc_label, max_gc_content = data_label, record_gc_content

    print max_gc_label
    print round(max_gc_content, 6)


if __name__ == '__main__':
    if len(argv) == 2:
        # something like 'python file.py test'
        import doctest
        doctest.testmod()
    else:
        compute_max_gc_content()
