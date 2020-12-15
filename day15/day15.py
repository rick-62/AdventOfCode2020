# day15
import sys
import re
from math import ceil, floor, gcd
from numpy import uint
from itertools import accumulate, combinations, count, permutations, product, repeat, chain
from collections import Counter, deque, namedtuple, defaultdict
from functools import lru_cache
from operator import add, mul
from copy import deepcopy


def puzzle(input, limit=2020):

    numbers = eval('[' + input[0] + ']')

    record = defaultdict(lambda: [0, 0])
    for i, n in enumerate(numbers, start=1):
        record[n] = [0, i]

    turn = len(numbers) + 1
    last = numbers[-1]

    for turn in count(start=turn):

        l1, l2 = record[last]
        spoken = (l2 - l1) if l1 > 0 else 0 

        record[spoken].append(turn)
        del record[spoken][0]

        last = spoken
                            
        if turn == limit:
            return spoken
            


if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()

    else:
        text = open('input.txt', 'r').readlines()
        
    print(f"Part 1: {puzzle(text, 2020)}")
    print(f"Part 2: {puzzle(text, 30000000)}")

    


