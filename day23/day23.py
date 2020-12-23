# day23
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from copy import deepcopy
from functools import lru_cache, reduce
from itertools import (accumulate, chain, combinations, count, cycle,
                       permutations, product, repeat)
from math import ceil, floor, gcd
from operator import add, mul, or_
from os import remove

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
    
    circle = deque([int(c) for c in input[0]])


    ''' Part 1 '''

    def remove_cups(circle, n=3):
        circle.rotate(-1)
        cups = [circle.popleft() for _ in range(n)]
        circle.rotate()
        return cups

    def destination_cup(circle):
        c = circle[0] - 1
        while c != -1:
            if c in circle: break
            c -= 1
        if c == -1: c = max(circle)
        return c

    def insert_cups(circle, cups, i):
        dest = circle.index(i)
        circle.rotate(-dest-1)
        circle.extendleft(cups[::-1])
        circle.rotate(dest+1)

    def next_cup(circle):
        circle.rotate(-1)

    def get_output(circle):
        i = circle.index(1)
        circle.rotate(-i)
        circle.popleft()
        return ''.join([str(c) for c in circle])

    test = deque([9,2,3,4,5,10])
    assert remove_cups(deque([9,2,3,4,5,10])) == [2,3,4]
    remove_cups(test)
    assert list(test) == [9,5,10]
    assert(destination_cup(test) == 5)
    insert_cups(test, [2,3,4], 5)
    assert list(test) == [9,5,2,3,4,10]
    next_cup(test)
    assert list(test) == [5,2,3,4,10,9]

    for _ in range(100):
        cups = remove_cups(circle)
        i = destination_cup(circle)
        insert_cups(circle, cups, i)
        next_cup(circle)

    p1 = get_output(circle)
    print(f"Part 1: {p1}")
  





if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()

    else:
        text = open('input.txt', 'r').readlines()
        
    puzzle(text)

    


