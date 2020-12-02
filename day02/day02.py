# day02
import sys
import re
from numpy import prod
from itertools import combinations
from collections import Counter, namedtuple


def puzzle(lines):

    # process input into named tuple
    pattern = re.compile(r'([0-9]+)-([0-9]+)\s([a-z]):\s([a-z]+)')
    pw = namedtuple('pw', ['min', 'max', 'char', 'word'])
    input = [pw(*pattern.findall(row)[0]) for row in lines]

    # print(input)

    p1 = 0
    p2 = 0
    for row in input:

        # part 1
        cnt = Counter(row.word)
        char_cnt = cnt[row.char]
        if int(row.min) <= char_cnt <= int(row.max):
            p1 += 1

        # part 2
        l1 = row.word[int(row.min)-1]
        l2 = row.word[int(row.max)-1]
        if (row.char in [l1, l2]) & (l1 != l2):
            p2 += 1


    print(f"Part 1: {p1} \t Part 2: {p2}")

    



    
        

if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()

    else:
        text = open('input.txt', 'r').readlines()

    puzzle(text)


