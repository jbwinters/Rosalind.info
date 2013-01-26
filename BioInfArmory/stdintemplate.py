#!/usr/bin/env python
from sys import stdin, argv

def main():
    """
    Given test:
    """
    for line in stdin:
        pass

if __name__ == '__main__':
    if len(argv) == 2:
        # something like 'python file.py test'
        import doctest
        doctest.testmod()
    else:
        main()
