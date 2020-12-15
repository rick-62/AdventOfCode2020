# day13
import sys
import re
from math import ceil, floor, gcd
from numpy import prod
from itertools import accumulate, count, repeat, chain
from collections import Counter, deque, namedtuple, defaultdict
from functools import lru_cache, reduce
from operator import add, mul
from copy import deepcopy


def puzzle(input):

    timestamp, ids = input
    timestamp = int(timestamp)

    ''' Part 1 '''
    buses = [int(id) for id in ids.split(',') if id != 'x']

    next_bus = max([(timestamp / bus % 1, bus) for bus in buses])[1] 

    p1 = (ceil(timestamp / next_bus) * next_bus - timestamp) * next_bus
    print(f"Part 1: {p1}")
    

    ''' Part 2 '''
    buses = [(int(id), i) for i, id in enumerate(ids.split(',')) if id != 'x']
    n = [id for id, _ in buses]
    a = [(id - i) * (i > 0) for id, i in buses]  

    def chinese_remainder(n, a):
        sum = 0
        prod = reduce(lambda a, b: a*b, n)
        for n_i, a_i in zip(n, a):
            p = prod // n_i
            sum += a_i * mul_inv(p, n_i) * p
        return sum % prod
    
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a // b
            a, b = b, a%b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1

    
    p2 = chinese_remainder(n, a)
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

    


