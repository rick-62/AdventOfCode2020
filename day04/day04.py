# day04
import sys
import re
from numpy import prod
from itertools import combinations
from collections import Counter, namedtuple


def puzzle(text):


    passports = [
        dict(e.split(':') for e in batch.split()) 
        for batch in text.split('\n\n')
        ]

    # part 1
    checks = {
        'byr', # (Birth Year)
        'iyr', # (Issue Year)
        'eyr', # (Expiration Year)
        'hgt', # (Height)
        'hcl', # (Hair Color)
        'ecl', # (Eye Color)
        'pid', # (Passport ID)
        #'cid', # (Country ID)
    }

    print(sum([checks.issubset(set(pp.keys())) for pp in passports]))






if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').read()

    else:
        text = open('input.txt', 'r').read()

    puzzle(text)


