# day03
import sys
import re
from numpy import prod
from itertools import combinations
from collections import Counter, namedtuple


def puzzle(lines):

    # strip each line
    map = [row.strip() for row in lines]

    # size of map segment
    w = len(map[0])
    h = len(map)

    def count_trees(E, S):
        i, j = 0, 0
        trees = 0
        for j in range(0, h, S):
            row = map[j]
            if row[i%w] == '#':
                trees += 1
            i += E
        return trees

    # part 1
    print(f"Part 1: {count_trees(3, 1)}")

    # part 2
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    trees = 1
    for E, S in slopes:
        trees *= count_trees(E, S)
    print(f"Part 2: {trees}")

           

if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()

    else:
        text = open('input.txt', 'r').readlines()

    puzzle(text)


