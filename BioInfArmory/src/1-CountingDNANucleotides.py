#!/usr/bin/env python

from sys import stdin
from collections import Counter

def main():
    sequence = stdin.next().upper()
    counts = Counter(sequence)
    print counts['A'], counts['C'], counts['G'], counts['T']

if __name__ == '__main__':
    main()
