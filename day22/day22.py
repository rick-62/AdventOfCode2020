# day22
import sys
import re
from math import ceil, floor, gcd
from numpy import uint
from itertools import cycle, accumulate, combinations, count, permutations, product, repeat, chain
from collections import Counter, deque, namedtuple, defaultdict
from functools import lru_cache, reduce
from operator import add, mul, or_
from copy import deepcopy


def puzzle(input):
    
    player1, player2 = [
       Deck([int(c) for c in p.strip().split('\n') if c.isnumeric()])
       for p in input.split('\n\n')
    ]

    player1.name = 'player 1'
    player2.name = 'player 2'

    ''' Part 1 '''

    while player1.cards and player2.cards:

        if player1.reveal > player2.reveal:
            player1.win(player2.pop_card)
        else:
            player2.win(player1.pop_card)


    p1 = player1.score + player2.score
    print(f"Part 1: {p1}")


    ''' Part 2 '''
    
    player1.reset()
    player2.reset()

    # Rules:
    # - if deck already player in this game for player, then player 1 wins game
    # - players begin each round by drawing their top card as normal
    # - if both players have at least as many remaining cards as value of card, then recurse
    # - if at least one player does not have enough cards to recurse, winner is highest card

    def play_game(p1, p2):

        while p1.cards and p2.cards:

            # print(str(p1.reveal), "vs", str(p2.reveal))
            # print("p1:", p1.cards, "\tp2:", p2.cards)
            
            # deck seen before - player1 wins game
            if p1.previous_deck or p2.previous_deck:
                return p1

            # card value greater than remaining then check highest
            elif (p1.reveal > p1.remaining) or (p2.reveal > p2.remaining):
                winner = p1 if p1.reveal > p2.reveal else p2
            
            # recurse if possible
            elif p1.sufficient_cards and p2.sufficient_cards:
                winner = play_game(p1.sub_deck, p2.sub_deck)

            # else highest card is winner
            else:
                winner = p1 if p1.reveal > p2.reveal else p2

            if winner.name == 'player 1':
                p1.win(p2.pop_card)
            elif winner.name == 'player 2':
                p2.win(p1.pop_card)
            else:
                raise AttributeError

        return p1 if p1.cards else p2


    p2 = play_game(player1, player2).score
    print(f"Part 2: {p2}")



class Deck:

    def __init__(self, cards, name=None):
        self.name = name
        self.cards = deque(cards)
        self.copy = deque(cards)
        self.history = set()

    @property
    def score(self):
        return sum([a * b for a, b in zip(reversed(self.cards), count(1))])

    @property
    def previous_deck(self):
        return tuple(self.cards) in self.history
        
    @property
    def reveal(self):
        return self.cards[0]

    @property
    def remaining(self):
        return len(self.cards)

    @property
    def sufficient_cards(self):
        return self.remaining > self.reveal

    @property
    def sub_deck(self):
        cnt = self.reveal
        new_cards = list(self.cards)[1:1+cnt]
        return Deck(new_cards, name=self.name)

    @property
    def pop_card(self):
        self.update_historic()
        return self.cards.popleft()

    def win(self, card):
        self.update_historic()
        self.cards.rotate(-1)
        self.cards.append(card)

    def update_historic(self):
        self.history.add(tuple(self.cards))

    def reset(self):
        self.cards = self.copy.copy()
        self.history.clear()

    def __repr__(self):
        return ','.join([str(x) for x in self.cards])





if __name__ == '__main__':

    print(sys.argv[0])

    if sys.argv[-1] == 'test':

        print("Testing...")

        text = open('test.txt', 'r').read()

    else:
        text = open('input.txt', 'r').read()
        
    puzzle(text)

    


