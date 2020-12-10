# day10
import sys
import re
from math import ceil, floor
from numpy import prod
from itertools import combinations, accumulate, islice
from collections import Counter, namedtuple, defaultdict
from functools import lru_cache


def puzzle(input):

    input = [int(n) for n in input]

    outlet = 0
    device = max(input) + 3
    adapters = [outlet] + sorted(input) + [device]

    ''' Part 1 '''
    diff = [y - x for x, y in zip(adapters, adapters[1:])]
    cnt = Counter(diff)
    p1 = cnt[3] * cnt [1]
    print(f"Part 1: {p1}")


    ''' Part 2 '''

    valid_adapters = defaultdict(list)
    for x, y in combinations(adapters, 2):
        if 0 < (y - x) <= 3:
            valid_adapters[x].append(y) 


    @lru_cache(maxsize=None)
    def arrangements(key=0):

        if key == device:
             return 1

        total = 0
        for adapter in valid_adapters[key]:
            total += arrangements(key=adapter)

        return total


    p2 = arrangements()
    print(f"Part 2: {p2}")





if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()
        puzzle(text)

    else:
        text = open('input.txt', 'r').readlines()
        puzzle(text)

    


