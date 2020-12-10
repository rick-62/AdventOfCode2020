# day10
import sys
import re
from math import ceil, floor
from numpy import prod
from itertools import combinations, accumulate, islice
from collections import Counter, namedtuple, defaultdict
from functools import lru_cache


def puzzle(input, preamble=25):

    input = [int(n) for n in input]

    adapters = [0] + sorted(input) + [max(input) + 3]

    ''' Part 1 '''
    diff = [y - x for x, y in zip(adapters, adapters[1:])]
    cnt = Counter(diff)
    p1 = cnt[3] * cnt [1]
    print(f"Part 1: {p1}")


    ''' Part 2 '''
    






if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()
        puzzle(text, preamble=5)

    else:
        text = open('input.txt', 'r').readlines()
        puzzle(text, preamble=25)

    


