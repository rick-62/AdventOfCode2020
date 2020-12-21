# day20
import sys
import re
from math import ceil, floor, gcd
from numpy import uint
from itertools import cycle, accumulate, combinations, count, permutations, product, repeat, chain
from collections import Counter, deque, namedtuple, defaultdict
from functools import lru_cache, reduce
from operator import add, mul, or_
from copy import deepcopy


def puzzle(input):
    
    allergens = defaultdict(set)

    def add_allergen(alg, ings):
        if alg not in allergens.keys():
            allergens[alg] = ings
        else:
            allergens[alg] = allergens[alg] & ings

    def remove_ingredient(ing):
        for alg, ings in allergens.items():
            if len(ings) > 1:
                allergens[alg].discard(ing)

    def count_ingredients():
        return sum([len(ings) for ings in allergens.values()])

    def matched_ingredients():
        return {
            list(ings)[0] for ings in allergens.values() 
            if len(ings) == 1
        }

    def ordered_ingredients():
        return [
            list(ings)[0] for _, ings in sorted(allergens.items())
            if len(ings) == 1
        ]

    # process input
    foods = (row.strip()[:-1].split(' (contains ') for row in input)
    all_ingredients = []
    for ings, algs in foods:
        ings_list = ings.split(' ')
        all_ingredients += ings_list
        for alg in algs.split(', '):
            add_allergen(alg, set(ings_list))
            
    # identify which ingredients refer to which allergens
    cnt = 0
    while cnt != count_ingredients():
        cnt = count_ingredients()
        for alg, ings in allergens.items():
            if len(ings) == 1:
                ing = list(ings)[0]
                remove_ingredient(ing)
    
    p1 = len([
        ing for ing in all_ingredients 
        if ing not in matched_ingredients()
    ])
    print(f"Part 1: {p1}")

    p2 = ','.join(ordered_ingredients())
    print(f"Part 2: {p2}")



if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()

    else:
        text = open('input.txt', 'r').readlines()
        
    puzzle(text)

    


