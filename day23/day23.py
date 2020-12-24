# day23
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from copy import deepcopy
from functools import lru_cache, reduce
from itertools import (accumulate, chain, combinations, count, cycle,
                       permutations, product, repeat, takewhile, islice)
from math import ceil, floor, gcd
from operator import add, mul, or_
from os import remove
from time import perf_counter

import numpy as np
from numpy import uint

# input of numbers arranged clockwise, in circle
# 1. start cup is first in string
# 2. 3 cups immediately clockwise removed
# 3. 1 removed from start cup until next label (distination cup)
# 4. immediately right of destination cup, add back 3 removed
# 5. next cup if next in list, after transformation
# 100 moved in total
# Part 1: combined string after the label 1 (100 iterations)
# Part 2: huge array, 10 millions iterations :(


def puzzle(input):
    

    def build_circle(dct, n=1):
        yield n 
        for i in range(len(dct)):
            n = dct[n]
            yield n

    def play_game(cups, moves, debug=True):

        circle = {k: v for k, v in zip(cups, cups[1:] + cups[:1])}
        mx = max(cups)
        curr = cups[0]

        for i in range(1, moves+1):
            cup1 = circle[curr]
            cup2 = circle[cup1]
            cup3 = circle[cup2]

            if debug: 
                print(f"-- move {i} --")
                print(f"cups: {' '.join([str(x) for x in build_circle(circle, curr)])}")
                print(f"pick up: {cup1}, {cup2}, {cup3}")

            circle[curr] = circle[cup3]

            dest = next(
                (
                    x for x in 
                    (curr-1, curr-2, curr-3, curr-4, mx, mx-1, mx-2) 
                    if ((x != cup1) and (x != cup2) and (x != cup3)) and (x > 0)
                )
            )

            if debug: 
                print(f"destination: {dest}", end="\n\n")

            circle[cup3] = circle[dest]
            circle[dest] = cup1
            curr = circle[curr]

        return circle

    ''' Part 1'''
    cups = [int(c) for c in input[0]]
    circle = play_game(cups, 100, debug=False)
    p1 = ''.join([str(x) for x in build_circle(circle) if x != 1])
    print(f"Part 1: {p1}")

    ''' Part2 '''
    cups = [int(c) for c in input[0]] + list(range(10, 1_000_001))
    circle = play_game(cups, 10_000_000, debug=False)
    circle_ = build_circle(circle)
    p2 = next(circle_) * next(circle_) * next(circle_)
    print(f"Part 2: {p2}")

    

if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()

    else:
        text = open('input.txt', 'r').readlines()
        
    puzzle(text)

    


