# day05
import sys
import re
from math import ceil, floor
from numpy import prod
from itertools import combinations
from collections import Counter, namedtuple


def puzzle(text):

    input = ((line[:7], line[7:10]) for line in text)

    # part 1
    seat_ids = {P(row) * 8 + P(col, 7) for row, col in input}
    print(f"Part 1: {max(seat_ids)}")

    # part 2
    expected = sum(range(min(seat_ids), max(seat_ids)+1))
    actual = sum(seat_ids)
    print(f"Part 2: {expected - actual}")


def P(L, mx=127, mn=0):

    if len(L) == 0:
        return mx
    
    if L[0] in 'RB':  # upper
        mn = ceil(mn + (mx - mn) / 2)
    
    if L[0] in 'FL':  # lower
        mx = floor(mx - (mx - mn) / 2)

    return P(L[1:], mx, mn)
    


if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        assert P('BFFFBBF') == 70
        assert P('FFFBBBF') == 14
        assert P('BBFFBBF') == 102
        assert P('RRR', 7) == 7
        assert P('RLL', 7) == 4

        text = open('test.txt', 'r').readlines()

    else:
        text = open('input.txt', 'r').readlines()

    puzzle(text)


