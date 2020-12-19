# day19
import sys
import re
from math import ceil, floor, gcd
from numpy import uint
from itertools import cycle, accumulate, combinations, count, permutations, product, repeat, chain
from collections import Counter, deque, namedtuple, defaultdict
from functools import lru_cache, reduce
from operator import add, mul, or_
from copy import deepcopy

# validate messages
# dictinary of values
# rules refer to other rules to build list of valid codes
# uses pipes for or operator - rules can have multiple combinations

# Part 1: determine number of messages which match rule 0
# Part 2: deal with rules with infinite loops


def puzzle(input):
    
    _rules, _messages = input.split('\n\n')

    rules = {
        k: v for k, v in 
        [
            rule.replace('"', '').split(': ') 
            for rule in _rules.split('\n')
        ]
    }

    messages = [msg for msg in _messages.split('\n')]


    ''' Part 1 '''

    def repl(matchobj):
        nxt = rules[matchobj.group(0)]
        if nxt in 'ab': return nxt
        return '(' + nxt + ')'


    @lru_cache(maxsize=None)
    def make_pattern(rule):

        rule, cnt = re.subn(r'\b(\d+)\b', repl, rule)

        if cnt > 0:
            return make_pattern(rule)
        
        return '^{}$'.format(rule.replace(' ', ''))
            


    # assert make_pattern('2') == '^(aa|bb)$'

    zero = make_pattern('0')
    p1 = sum([1 if re.match(zero, msg) else 0 for msg in messages])

    print(f"Part 1: {p1}")


    ''' Part 2 '''

    # rules updated with infinite loops
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31

    rules.update(
        {
            '8': '42 +', 
            '11': '42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31'
        }
    )

    make_pattern.cache_clear()

    zero = make_pattern('0')
    # print(zero)
    
    p2 = sum([1 if re.match(zero, msg) else 0 for msg in messages])

    print(f"Part 2: {p2}")


















    

if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').read()

    else:
        text = open('input.txt', 'r').read()
        
    puzzle(text)

    


