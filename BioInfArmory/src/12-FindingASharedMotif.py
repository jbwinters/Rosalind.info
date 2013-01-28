#!/usr/bin/env python
from sys import stdin, argv
import re
from utilities import substrings

def longest_common_substring(strings=None):
    r"""
    Not a very efficient solution

    Given test:
    >>> strings = '''GATTACA
    ... TAGACCA
    ... ATACA'''
    >>> longest_common_substring(strings)
    TA
    """
    if not strings:
        strings = stdin.read().strip()
    strings = strings.split()
    shortest_str = min(((len(x), x) for x in strings))[1]
    strings.remove(shortest_str)

    longest_common_substring = ''
    for sub in substrings(shortest_str):
        if all(sub in string for string in strings):
            longest_common_substring = sub
            break
    print longest_common_substring


if __name__ == '__main__':
    if len(argv) == 2:
        # something like 'python file.py test'
        import doctest
        doctest.testmod()
    else:
        longest_common_substring()
