# day14
import sys
import re
from math import ceil, floor, gcd
from numpy import uint
from itertools import accumulate, combinations, count, permutations, product, repeat, chain
from collections import Counter, deque, namedtuple, defaultdict
from functools import lru_cache
from operator import add, mul
from copy import deepcopy


def puzzle(input):


    ''' Part 1 '''
    mem = defaultdict(uint)

    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for line in input:
        m, n = line.strip().split(' = ')
        if m == 'mask':
            mask = n
        else:
            b = str(bin(int(n)))[2:].zfill(len(mask))
            b = '0b' + ''.join(x if x != 'X' else a for x, a in zip(mask, b))
            exec(m + ' = ' + b)

    p1 = sum(mem.values())
    print(f"Part 1: {p1}")


    ''' Part 2 '''
    mem = defaultdict(uint)

    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for line in input:
        m, n = line.strip().split(' = ')
        if m == 'mask':
            mask = n
        else:
            # extract target memory address
            addr = int(re.search(r'\[(\d+)\]', m)[1])

            # get bitwise maximum between addr and mask
            b = '0b' + ''.join(
                max(x) if max(x) != 'X' else '{}'  for x 
                in zip(mask, str(bin(addr))[2:].zfill(len(mask)))
                )

            # somehow, for every combination of Xs
            float = (b.format(*combo) for combo in product('01', repeat=b.count('{')))

            # store n in each location
            for addr in float:
                mem[addr] = int(n)


    p2 = sum(mem.values())
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

    


