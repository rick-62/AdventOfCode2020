# day24
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

# new tiles floor being installed in lobby
# tiles are hexagonal
# arranged in a hex grid
# very specific colour pattern
# tiles are white on one side and black on other
# tiles begin white side up
# lobby assumed to be infinite
# list of tiles which require flipping (input)
# each tile has 6 neighbours: e, se, sw, w, nw, ne
# tile identified by series of these directions from reference tile
# each time a tile identified it flips (white to black, or black to white)
# Part 1: after instructions followed, how many black side up?

# part 2:
# a black tile (1) with 0 or >2 adjacent black tiles is flipped
# white tile (0) with 2 adjacent black tiles is flipped


def puzzle(input):
    
    # regex to get list of instructions
    # defaultdict
    # each tile tuple of coordinate, as dict key
    # use hex geometry

    def add_(c, v):
        return (c[0] + v[0], c[1] + v[1])

    dir_ref = {
        'nw': ( 1, -1),
        'ne': ( 1,  1),
        'sw': (-1, -1),
        'se': (-1,  1),
        'e':  ( 0,  2),
        'w':  ( 0, -2),
    }

    tiles = defaultdict(lambda:0)


    ''' Part 1 '''

    for line in input:
        curr = (0, 0)
        instruction = re.findall(r'nw|ne|sw|se|e|w', line)
        vectors = (dir_ref[dir] for dir in instruction)
        for v in vectors:
            curr = add_(curr, v)
        tiles[curr] ^= 1
    
    p1 = sum(tiles.values())
    print(f"Part 1: {p1}")


    ''' Part 2 '''

    def adjacent(tile):
        return {add_(tile, dir) for dir in dir_ref.values()}

    for day in range(1, 101):

        # print(f"Day {day}: ", end='')

        black = [k for k, v in tiles.items() if v]
        to_flip = set()

        for tile in black:

            adj_black = {adj for adj in adjacent(tile)}

            # rule 1
            n_black = sum([tiles[adj] for adj in adj_black])
            if (n_black == 0) or (n_black > 2):
                to_flip.add(tile)

            # rule 2
            white = {adj for adj in adj_black if tiles[adj] == 0}
            for tile in white:
                adj_white = {adj for adj in adjacent(tile)}
                n_black = sum([tiles[adj] for adj in adj_white])
                if n_black == 2:
                    to_flip.add(tile)

        for tile in to_flip:
            tiles[tile] ^= 1

        # print(f"{sum(tiles.values())}")
    
    p2 = sum(tiles.values())
    print(f"Part 1: {p2}")





        







        





    pass

    
if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()

    else:
        text = open('input.txt', 'r').readlines()
        
    puzzle(text)

    


