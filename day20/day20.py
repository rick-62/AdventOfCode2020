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

# randomly oriented square tiles
# combined together to form a new square array
# borders must match exactly, but could be flipped
# borders at the edges match with no other borders
# identify the corner tiles
# Part 1: multiply corners - corners can only be adjacent to 2 borders

# remove borders from each tile
# identify monster(s):
                        # 
        #    ##    ##    ###
        #  #  #  #  #  #   
# Part 2: count remaing "#" after removing monsters


def puzzle(input):
    
    tiles = {
        Tile(int(i[5:]), t.split('\n')) 
        for i,t in 
        [raw.split(':\n') for raw in input.split('\n\n')]
        }

    dim = int(len(tiles) ** (1/2))


    ''' Part 1 '''

    # identify matching borders between tiles
    borders = {t.id: t.borders for t in tiles}
    matches = defaultdict(list)
    for t in tiles:
        matches[t.id] = [
            id for id, bset in borders.items() 
            if any(t.borders.intersection(bset)) and (id != t.id)
            ]

    # identify the corner tiles
    corners = [id for id, adj in matches.items() if len(adj) == 2]
    assert len(corners) == 4

    p1 = reduce(lambda x,y: x*y, corners)
    print(f"Part 1: {p1}")


    ''' Part 2 '''

    # need to know array of tile ids
    image = defaultdict(int)

    # first row
    image[(0,0)] = corners[0]
    adj = image[(0,0)]
    for i in range(1, dim):
        links = [
            id for id in matches[adj] 
            if len(matches[id]) <= 3 and id not in image.values()
            ]
        adj = links[0]
        image[(0,i)] = adj

    # remaining tiles
    for j,i in product(range(1, dim), range(dim)):
        adj = image[(j-1,i)]  # tile above
        links = [id for id in matches[adj] if id not in image.values()]
        adj = links[0]
        image[(j,i)] = adj

    # print_dct(image)


    # need to know the orientation of each tile

    def get_tile(id):
        for t in tiles:
            if t.id == id:
                return t 

    def get_adjacent(coord):
        directions = {
            'right': (0,1), 'left': (0,-1), 
            'top': (-1, 0), 'bottom': (1,0),
        }
        return {
            name: tuple(a+b for a,b in zip(coord,dir)) 
            for name, dir in directions.items()
        }

    # loop through tiles, transform and check border match to adjacent
    for coord, id in image.items():
        adj_coords = get_adjacent(coord)
        adj_tiles = {
            name: get_tile(image[tile])
            for name, tile in adj_coords.items() 
            if tile in image.keys()
        }
        tile = get_tile(id)
        for transformation in ['r90']*4 + ['flipx'] + ['r90']*4:
            tile.transform(transformation)
            if all([
                ''.join(tile.border(orientation=orientation)) in adj_tile.borders
                for orientation, adj_tile in adj_tiles.items()
            ]): 
                tile.transformed = True
                break

    # print_2darray(tile.cam)

    assert all([tile.transformed for tile in tiles])
      
    # remove borders from each tile
    for tile in tiles:
        tile.remove_borders()

    # combine tiles to create the image
    actual_image = []
    for row in range(0, dim):
        row = [get_tile(id).cam for (j,i),id in sorted(image.items()) if j == row]
        actual_image.append([''.join(list(chain(*row))) for row in (zip(*row))])
    actual_image = list(chain(*actual_image))


    # identify monster(s) in 2D array
                          # 
    #    ##    ##    ###
     #  #  #  #  #  # 

    m2 = re.compile(r'#....##....##....###')
    m3 = re.compile(r'^.#..#..#..#..#..#')
    def find_monster(j, image):
        matches2 = {m.start(0) for m in re.finditer(m2, image[j-1])}
        matches3 = {start for start in matches2 if re.match(m3, image[j][start:])}
        return sum([1 for monster in matches3 if image[j-2][monster+18] == '#'])

    def count_monsters(image):
        total_monsters = 0
        for j, row in enumerate(image[2:], 2):
            total_monsters += find_monster(j, image)
        return total_monsters

    cnt = 0
    for transformation in ['r90']*4 + ['flipx'] + ['r90']*4:
        actual_image = [''.join(v) for v in Tile.transformations[transformation](actual_image)]
        # print_2darray(actual_image)
        cnt = count_monsters(actual_image)
        if cnt > 0:
            break
    
    p2 = sum([Counter(row)['#'] for row in actual_image]) - cnt * 15
    print(f"Part 2: {p2}")

   


class Tile:
    transformations = {
        'flipx': lambda X: [r[::-1] for r in X],
        'flipy': lambda X: X[::-1],
        'r90': lambda X: list(zip(*X[::-1]))
    }

    def __init__(self, id, cam) -> None:
        self.id = id
        self.cam = cam
        self.borders = self.get_borders()
        self.transformed = False

    def get_borders(self):
        top = self.border(orientation='top')
        bottom = self.border(orientation='bottom')
        left = self.border(orientation='left')
        right = self.border(orientation='right')

        return {
            top, top[::-1], 
            bottom, bottom[::-1], 
            left, left[::-1] , 
            right, right[::-1]  
        }

    def border(self, orientation='right'):
        if orientation == 'right':
            return ''.join([row[-1] for row in self.cam])
        elif orientation == 'left':
            return ''.join([row[0] for row in self.cam])
        elif orientation == 'bottom':
            return self.cam[-1]
        elif orientation == 'top':
            return self.cam[0]
        else:
            raise ValueError

    def transform(self, transform='r90'):
        if not self.transformed:
            self.cam = self.transformations[transform](self.cam)

    def remove_borders(self):
        del self.cam[0]
        del self.cam[-1]
        self.cam = [row[1:-1] for row in self.cam]

    def __repr__(self):
        return str(self.id)


def print_dct(coords):
    for row in range(0, max(coords.keys())[0] + 1):
        print([v for (j,i), v in sorted(coords.items()) if j == row ])
    print('\n')

def print_2darray(coords):
    for row in coords:
        print(''.join(x for x in row))
    print('\n')




if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').read()

    else:
        text = open('input.txt', 'r').read()
        
    puzzle(text)

    


