# day05
import sys
import re
from math import ceil, floor
from numpy import prod
from itertools import combinations
from collections import Counter, namedtuple

from numpy.core.function_base import linspace


def puzzle(text):


    # part 1
    groups = [
        {e for e in batch.replace('\n', '')} 
        for batch in text.split('\n\n')
        ]

    p1 = sum([len(g) for g in groups])
    print(f"Part 1: {p1}")


    # part 2
    groups = [
        [set(e) for e in batch.split('\n')]
        for batch in text.split('\n\n')
        ]

    p2 = sum([len(g[0].intersection(*g)) for g in groups])
    print(f"Part 2: {p2}")




if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').read()

    else:
        text = open('input.txt', 'r').read()

    puzzle(text)


