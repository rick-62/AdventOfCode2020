# day17
import sys
import re
from math import ceil, floor, gcd
from numpy import uint
from itertools import cycle, accumulate, combinations, count, permutations, product, repeat, chain
from collections import Counter, deque, namedtuple, defaultdict
from functools import lru_cache, reduce
from operator import add, mul, or_
from copy import deepcopy


# active and inactive cubes
# each cube represented by xyz coordinate
# 3D zspace is infinite
# Each cube has 26 neighbours, where their coorindate differs by at most 1
# During a cycle, all cubes change state simultaneously
# if cube is active and exactly 2 or 3 are also active, then cube remains active
# if cube is inactive but exactly 3 neighbours are active, the cube becomes active

# Part 1: configuration of cubes after 6 cycles?
# Part 2: in 4 dimensions

def puzzle(input, dimensions=3):

    active_cubes = {
        (i, j, 0) if dimensions == 3 else (i, j ,0, 0)
        for j, line in enumerate(input) 
        for i, cube in enumerate(line) 
        if cube == '#'
    }

    def get_neighbours(coord):
        adjacent_coords = product(*((x, x+1, x-1) for x in coord))
        return {c for c in adjacent_coords if c != coord}
        
    assert len(get_neighbours((0,1,1))) == 26
    assert len(get_neighbours((0,1,1,1))) == 80

    def count_active_neighbours(coord, active_cubes):
        neighbours = get_neighbours(coord)
        return len(neighbours.intersection(active_cubes))

    for cycle in range(6):
            
        deactivate = {
            cube for cube in active_cubes 
            if count_active_neighbours(cube, active_cubes) not in [2,3]
        }

        adjacent = reduce(
            or_, (get_neighbours(cube) for cube in active_cubes)
        )

        inactive_neighbours = adjacent - active_cubes

        activate = {
            cube for cube in inactive_neighbours 
            if len(active_cubes & get_neighbours(cube)) == 3
        }
        
        active_cubes |= activate
        active_cubes -= deactivate

    return len(active_cubes)


if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()

    else:
        text = open('input.txt', 'r').readlines()
        
        
    p1 = puzzle(text)
    p2 = puzzle(text, dimensions=4)
    print(f"Part 1: {p1} \nPart 2: {p2}")

    


