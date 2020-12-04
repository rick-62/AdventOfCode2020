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

    checks = {
        'byr': re.compile(r'^19[2-9][0-9]|200[0-2]$') ,                           # (Birth Year)
        'iyr': re.compile(r'^201[0-9]|2020$') ,                                   # (Issue Year)
        'eyr': re.compile(r'^202[0-9]|2030$') ,                                   # (Expiration Year)
        'hgt': re.compile(r'^1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in$') ,  # (Height)
        'hcl': re.compile(r'^#[0-9a-f]{6}$') ,                                    # (Hair Color)
        'ecl': re.compile(r'^amb|blu|brn|gry|grn|hzl|oth$') ,                     # (Eye Color)
        'pid': re.compile(r'^[0-9]{9}$') ,                                        # (Passport ID)
        #'cid', # (Country ID)
    }

    # part 1
    field_check = [set(checks.keys()).issubset(pp.keys()) for pp in passports]
    print(f"Part 1: {sum(field_check)}")

    # part 2
    cnt = 0
    for pp, valid in zip(passports, field_check):
        cnt += all([re.match(v, pp[k]) for k,v in checks.items()]) if valid else 0
    print(f"part 2: {cnt}")

            



if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').read()

    else:
        text = open('input.txt', 'r').read()

    puzzle(text)


