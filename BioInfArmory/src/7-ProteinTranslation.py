#!/usr/bin/env python
from sys import stdin, argv
from utilities import codon_to_protein_dct

def translate_to_protein_string(sequence=None):
    """
    Given test:
    >>> seq = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    >>> translate_to_protein_string(seq)
    MAMAPRTEINSTRING
    """
    if not sequence:
        sequence = stdin.next().strip()
    protein_list = []
    for codon_start_index in range(0, len(sequence), 3):
        codon = sequence[codon_start_index:codon_start_index + 3]
        protein = codon_to_protein_dct[codon]
        if protein == 'Stop':
            break
        protein_list.append(protein)
    print ''.join(protein_list)

if __name__ == '__main__':
    if len(argv) == 2:
        # something like 'python file.py test'
        import doctest
        doctest.testmod()
    else:
        translate_to_protein_string()
