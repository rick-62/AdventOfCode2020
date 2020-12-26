# day25
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from copy import deepcopy
from functools import lru_cache, reduce
from itertools import (accumulate, chain, combinations, count, cycle, islice,
                       permutations, product, repeat, takewhile)
from math import ceil, floor, gcd
from operator import add, mul, or_
from os import remove
from time import perf_counter

import numpy as np
from numpy import uint

# start with value of 1
# try different loop sizes (prime number?)
# in each loop do the following:
    # value = value * subject number 
    # value = value % 20201227
# correct loop size when value = public key (input)
# Part 1: use loop size on other public key to get answer
# Part 2: have all previous stars :)

def puzzle(input):
    
    public1, public2 = [int(k) for k in input]

    def loop(value, subject):
        value *= subject
        value = value % 20201227
        return value

    def find_loop(value=1, subject=7):
        for n in count(1):
            value = loop(value, subject)
            if value == public1:
                return n

    def decrypt(loop_n, value=1):
        for n in count(1):
            value = loop(value, public2)
            if n == loop_n:
                return value
    
    p1 = decrypt(find_loop())
    print(f"Part 1: {p1}")



    
if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()

    else:
        text = open('input.txt', 'r').readlines()
        
    puzzle(text)

    


