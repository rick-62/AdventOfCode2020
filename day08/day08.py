# day05
import sys
import re
from math import ceil, floor
from numpy import prod
from itertools import combinations
from collections import Counter, namedtuple, defaultdict
from functools import lru_cache


def puzzle(input):


    ''' Part 1 '''

    boot = Boot(input)
    print(f"Part 1: {boot.part1()}")


    ''' Part 2 '''

    def modify(input, i):
        input = input.copy()
        line = input[i]
        if 'jmp' in line:
            input[i] = line.replace('jmp', 'nop')
        else:
            input[i] = line.replace('nop', 'jmp')
        return input

    for i in range(len(input)):
        modified = modify(input, i)
        if modified == input:
            continue
        boot = Boot(modified)
        p2 = boot.part2()
        if p2:
            print(f"Part 2: {p2}")
            break




class Boot:

    def __init__(self, input) -> None:
        self.accumulator = 0
        self.pointer = 0
        self.record = []
        self.input = input
    
    def part1(self):
        while self.pointer not in self.record:
            self.record.append(self.pointer)
            i, v = self.input[self.pointer].split()
            getattr(self, i)(int(v))
        return self.accumulator

    def part2(self):
        lines = len(self.input)
        while self.pointer < lines:
            self.record.append(self.pointer)
            i, v = self.input[self.pointer].split()
            getattr(self, i)(int(v))
            if self.pointer in self.record:
                return False
        return self.accumulator

    def acc(self, a):
        self.accumulator += a
        self.pointer += 1

    def jmp(self, a):
        self.pointer += a

    def nop(self, *args):
        self.pointer += 1





if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()

    else:
        text = open('input.txt', 'r').readlines()

    puzzle(text)


