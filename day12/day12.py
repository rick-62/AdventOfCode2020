# day12
import sys
import re
from math import ceil, floor
from numpy import prod
from itertools import combinations, accumulate, product, count
from collections import Counter, deque, namedtuple, defaultdict
from functools import lru_cache
from operator import add, mul
from copy import deepcopy


def puzzle(input):

    NESW = {'N': 0+1j, 'E': 1+0j, 'S': 0-1j, 'W': -1+0j}

    ''' Part 1 '''
    RL = {'R': -1, 'L': 1}
    direction = deque('ESWN')
    loc = 0 + 0j
    for line in input:
        d, v = line[0], int(line[1:])
        direction.rotate(RL.get(d,0) * int(v/90))
        D = direction[0] if d == 'F' else d
        loc += NESW.get(D, 0) * v

    p1 = sum([abs(loc.real), abs(loc.imag)])
    print(f"Part 1: {p1}")


    ''' Part 2 '''
    waypoint = 10 + 1j
    RL = {'R': -1j, 'L': 1j}
    loc = 0 + 0j
    for line in input:
        d, v = line[0], int(line[1:])
        waypoint *= RL.get(d,1) ** int(v/90)
        waypoint += NESW.get(d,0) * v
        if d == 'F': loc += waypoint * v 

    p2 = sum([abs(loc.real), abs(loc.imag)])
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

    


