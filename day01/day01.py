# day01
import sys
from numpy import prod
from itertools import combinations


def puzzle(lines, r=2):

    input = [int(row.strip('\n')) for row in lines]

    for group in combinations(input, r):
        if sum(group) == 2020:
            return(prod(group))
        

if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()

    else:
        text = open('input.txt', 'r').readlines()


    print(f"Part 1: {puzzle(text)}")
    print(f"Part 2: {puzzle(text, r=3)}")

