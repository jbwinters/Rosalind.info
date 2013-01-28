#!/usr/bin/env python
from sys import stdin, argv

def calculate_expected_offspring(population=None):
    """
    Given test:
    >>> population = '1 0 0 1 0 1'
    >>> calculate_expected_offspring(population)
    3.5
    """
    if not population:
        population = stdin.read().strip()
    num_offspring_per_couple = 2
    population = [int(x) for x in population.split()]
    homdom_offspring_frequencies = [1., 1., 1., .75, .5, 0]
    homdom_offspring = 0
    for num_inds, freq in zip(population, homdom_offspring_frequencies):
        homdom_offspring += num_inds * freq
    homdom_offspring *= num_offspring_per_couple
    print homdom_offspring

if __name__ == '__main__':
    if len(argv) == 2:
        # something like 'python file.py test'
        import doctest
        doctest.testmod()
    else:
        calculate_expected_offspring()
