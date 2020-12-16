# day16
import sys
import re
from math import ceil, floor, gcd
from numpy import uint
from itertools import cycle, accumulate, combinations, count, permutations, product, repeat, chain
from collections import Counter, deque, namedtuple, defaultdict
from functools import lru_cache, reduce
from operator import add, mul
from copy import deepcopy


def puzzle(input):


    ''' Extracting the input '''

    _rules, _my_ticket, _nearby = input.split('\n\n')

    rules = {
        field: [int(v) for v in re.findall(r'\d+', limit)] 
        for field, limit 
        in [rule.split(': ') for rule in _rules.split('\n')]
    }

    def extract_ticket(text):
        return [
            eval('[' + row + ']') 
            for row in text.split('\n') 
            if 'ticket' not in row
        ]

    my_ticket = extract_ticket(_my_ticket)[0]
    nearby = extract_ticket(_nearby)


    ''' Part 1 '''

    def is_valid(value):
        for l1, h1, l2, h2 in rules.values():
            if l1 <= value <= h1:
                return True
            if l2 <= value <= h2:
                return True
        return False

    invalid_values = [
        value
        for ticket in nearby 
        for value in ticket 
        if not is_valid(value)
        ]

    p1 = sum(invalid_values)
    print(f"Part 1: {p1}")


    ''' Part 2 '''
    
    def valid_fields(value, found):
        return {
            field for field, (l1, h1, l2, h2) in rules.items() 
            if (field not in found.keys()) and 
            ((l1 <= value <= h1) or (l2 <= value <= h2))
        }

    def get_indices(found={}):

        if len(found) == n_field:
            return found

        for i in range(n_field):
            field = [valid_fields(t[i], found) for t in valid_tickets]
            common = set.intersection(*field)
            if len(common) == 1:
                found[common.pop()] = i
        
        return get_indices(found=found)


    n_field = len(my_ticket)

    valid_tickets = [my_ticket] + [
        ticket for ticket in nearby
        if all([is_valid(v) for v in ticket])
    ] 

    p2 = reduce(
        lambda x,y: x*y, 
        [my_ticket[i] for f, i in get_indices().items() 
        if f.startswith('depart')]
    )

    print(f"Part 2: {p2}")





if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').read()
        puzzle(text)

    else:
        text = open('input.txt', 'r').read()
        puzzle(text)

    


