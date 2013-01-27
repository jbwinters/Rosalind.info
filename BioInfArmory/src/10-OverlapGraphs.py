#!/usr/bin/env python
from sys import stdin, argv
from utilities import FASTA_Dataset
from collections import defaultdict

class Node(object):
    def __init__(self):
        self.labels = set()
        self.neighbors = set()

    def __iter__(self):
        for label in self.labels:
            for neighbor in self.neighbors:
                if label != neighbor:
                    yield (label, neighbor)

def overlap_graph(dataset=None):
    r"""
    Given test:
    >>> dataset = '''>Rosalind_0498
    ... AAATAAA
    ... >Rosalind_2391
    ... AAATTTT
    ... >Rosalind_2323
    ... TTTTCCC
    ... >Rosalind_0442
    ... AAATCCC
    ... >Rosalind_5013
    ... GGGTGGG'''
    >>> overlap_graph(dataset)
    Rosalind_0498 Rosalind_0442
    Rosalind_0498 Rosalind_2391
    Rosalind_2391 Rosalind_2323
    """
    if not dataset:
        dataset = stdin.read().strip()
    sequences = FASTA_Dataset(dataset)
    prefix_table = defaultdict(Node)

    k = 3
    for label, seq in sequences:
        prefix = seq[0:k]
        suffix = seq[-k:]
        prefix_table[suffix].labels.add(label)
        prefix_table[prefix].neighbors.add(label)

    for node in prefix_table.itervalues():
        for node, neighbor in node:
            print node, neighbor

if __name__ == '__main__':
    if len(argv) == 2:
        # something like 'python file.py test'
        import doctest
        doctest.testmod()
    else:
        overlap_graph()
