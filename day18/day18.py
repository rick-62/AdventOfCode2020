# day18
import sys
import re
from math import ceil, floor, gcd
from numpy import uint
from itertools import cycle, accumulate, combinations, count, permutations, product, repeat, chain
from collections import Counter, deque, namedtuple, defaultdict
from functools import lru_cache, reduce
from operator import add, mul, or_
from copy import deepcopy

from numpy.lib.function_base import extract

# evalute expression
# but in sequenced order, not arithmetic order
# but braces always evaluated first
# can have braces within braces
# only + and *

# Part 1: sum of expressions


def puzzle(input):
    

    ''' Part 1 '''

    def evaluate(x):
        if x.isnumeric():
            return int(x)
        e, x = re.findall(r'^(\d+\s[\+\*]\s\d+)(.+)?', x)[0]
        ans = eval(e)
        return ans if not x else evaluate(str(ans) + x)

    def has_brackets(x):
        return '(' in x

    def evaluate_all(x):

        if not has_brackets(x):
            return evaluate(x)

        m = re.match(r'(.+)?\(([^\(]+?)\)(.+)?', x)
        prefix = m.group(1) if m.group(1) else ''
        suffix = m.group(3) if m.group(3) else ''
        ans = str(evaluate(m.group(2)))

        return evaluate_all(prefix + ans + suffix)


    assert evaluate_all('(9 * 8) + (6 * 7)') == 114
    assert evaluate('5 + 6 * 6 + 5') == 71
    assert evaluate('5 * 6') == 30
    assert has_brackets('(6 + 8)') == True
    assert has_brackets('6 + 8') == False

    p1 = sum([evaluate_all(x) for x in input])
    print(f"Part 1: {p1}")


    ''' Part 2 '''

    def evaluate_addition(x):

        if '+' not in x:
            return evaluate(x)

        m = re.match(r'(.+)?\b(\d+\s\+\s\d+)\b(.+)?', x)
        prefix = m.group(1) if m.group(1) else ''
        suffix = m.group(3) if m.group(3) else ''
        ans = str(evaluate(m.group(2)))

        return evaluate_addition(prefix + ans + suffix)


    def evaluate_all(x, p=False):

        if not has_brackets(x):
            return evaluate_addition(x)

        m = re.match(r'(.+)?\(([^\(]+?)\)(.+)?', x)
        prefix = m.group(1) if m.group(1) else ''
        suffix = m.group(3) if m.group(3) else ''
        ans = str(evaluate_addition(m.group(2)))
        if p: print(prefix + ans + suffix)

        return evaluate_all(prefix + ans + suffix, p=p)


    assert evaluate_all('1 + (2 * 3) + (4 * (5 + 6))') == 51
    assert evaluate_all('2 * 3 + (4 * 5)') == 46
    assert evaluate_all('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 1445
    assert evaluate_all('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 669060
    assert evaluate_all('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', p=True) == 23340


    p2 = sum([evaluate_all(x) for x in input])
    print(f"Part 2: {p2}")

    

if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()

    else:
        text = open('input.txt', 'r').readlines()
        
    puzzle(text)

    


