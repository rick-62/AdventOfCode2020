# day05
import sys
import re
from math import ceil, floor
from numpy import prod
from itertools import combinations, accumulate, islice
from collections import Counter, namedtuple, defaultdict
from functools import lru_cache


def puzzle(input, preamble=25):

    input = tuple([int(n) for n in input])


    ''' Part 1 '''
    invalid = [
        n for i, n in enumerate(input[preamble:]) 
        if not any(
            [
                sum(pair) == n for pair 
                in combinations(input[i:preamble+i], 2)]
        )
    ]

    p1 = invalid[0]
    print(f"Part 1: {p1}")


    ''' Part 2 '''
    for i,_ in enumerate(input):

        match = [
            min(input[i:i+j]) + max(input[i:i+j]) 
            for j, v in enumerate(accumulate(input[i:])) 
            if v == p1
            ]
            
        if match:
            print(f"Part 2: {match[0]}")
            break

    

if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()
        puzzle(text, preamble=5)

    else:
        text = open('input.txt', 'r').readlines()
        puzzle(text, preamble=25)

    


