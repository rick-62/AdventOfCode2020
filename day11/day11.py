# day11
import sys
import re
from math import ceil, floor
from numpy import prod
from itertools import combinations, accumulate, product, count
from collections import Counter, namedtuple, defaultdict
from functools import lru_cache
from operator import add, mul
from copy import deepcopy


def puzzle(input):

    # coordinates of the seating area
    # "\n" assumed to be floor
    seating = dict(
        ((j, i), 'seat') if seat == 'L' 
        else ((j, i), 'floor')
        for j, row  in enumerate(input) 
        for i, seat in enumerate(row) 
        )

    # seat oject class
    class Seat:
        adj_coords = list(product([0,1,-1], repeat=2))
        
        def __init__(self, coord) -> None:
            self.coord = coord
            self.occupied = 0
            self.change = True
            self.adj_occupied = 0
            self.adjacent = self._get_adjacent()
            self.visible = self._get_visible()

        def _get_adjacent(self):
            adjacent = {
                tuple(map(add, adj, self.coord))
                for adj in self.adj_coords
                if adj != (0, 0)  # remove self
            }
            return adjacent

        def _get_visible(self):

            def get_coord(dir):
                for i in count(1):
                    xdir = [i * x for x in dir]
                    viz = tuple(map(add, xdir, self.coord))
                    if (viz not in seating.keys()) or (viz == self.coord):
                        return None
                    elif (seating[viz] == 'seat'):
                        return viz

            return [
                v for v in 
                [get_coord(dir) for dir in self.adj_coords] 
                if v != None
                ]


        def __repr__(self) -> str:
            return str(self.coord) + ' ' + str(self.occupied)


    seats = {
        coord: Seat(coord) 
        for coord, val in seating.items() 
        if val == 'seat'
        }

    
    def part(seats, method='adjacent', x=4, print_on=False):

        seats = deepcopy(seats)
    
        while any(seat.change for seat in seats.values()):

            # change all seat occupancy values
            for seat in seats.values():
                if seat.change:
                    seat.occupied ^= 1
                    seat.change = False

            if print_on: printer(input, seats)

            # check which seats need to toggle occupancy
            for seat in seats.values():
                adj_occupied = [seats[adj].occupied if adj in seats.keys() else 0 for adj in getattr(seat, method)]

                # leave seat if 4 or more adjacent occupied
                if seat.occupied:
                    if sum(adj_occupied) >= x:
                        seat.change = True
                
                # sit in seat if no adjacent occupied
                else:
                    if not any(adj_occupied):
                        seat.change = True

        return sum([s.occupied for s in seats.values()])

        
    p1 = part(seats, method='adjacent')
    print(f"Part 1: {p1}")

    p2 = part(seats, method='visible', x=5)
    print(f"Part 2: {p2}")
        


def printer(puzzle, seats):
    puzzle = [list(row) for row in puzzle]
    for (i,j), v in seats.items():
        puzzle[i][j] = 'L' if v.occupied == 0 else '#'
    for row in puzzle:
        print(''.join(row), end='')
    print('\n')
    


if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').readlines()
        puzzle(text)

    else:
        text = open('input.txt', 'r').readlines()
        puzzle(text)

    


