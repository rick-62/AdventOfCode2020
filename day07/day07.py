# day05
import sys
import re
from math import ceil, floor
from numpy import prod
from itertools import combinations
from collections import Counter, namedtuple, defaultdict
from functools import lru_cache


def puzzle(text, target='shiny gold'):

    # convert input to dictionary
    # {bag: [bag, bag, bag, bag, ...]}
    bags = defaultdict(list)
    for line in text:
        bag, contents = line.split(' bags contain ')
        bags[bag] = re.findall(r'(\d+)\s(.+?)\sbag', contents)

    ''' Part 1 '''

    @lru_cache(maxsize=None)
    def check(bag):
        # recursive function with caching
        if bag == target:
            return True
        return any({check(c) for _,c in bags[bag]})

    p1 = sum([check(bag) for bag in bags.keys()]) - 1 # shiny gold itself is removed
    print(f"Part 1: {p1}")


    ''' Part 2 '''
    
    @lru_cache(maxsize=None)
    def count(bag=target, total=0):
        # recursive function with caching
        for q,c in bags[bag]:
            total += int(q) + int(q) * count(c)
        return total

    print(f"Part 2: {count()}")







if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()

    else:
        text = open('input.txt', 'r').readlines()

    puzzle(text)


