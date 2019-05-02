# Deck.py
# Authors: Jamal Almouslli, Kevin Mooney

import PlayingCard
import random


class Deck:

    cards = []
    card_type = ''

    def __init__(self):
        self.cards = []
        for suit in ['C', 'H', 'D', 'S']:
            for rank in range(1, 14):
                card = PlayingCard.PlayingCard(suit, rank)
                self.cards.append(card)

    def deal(self):
        if self.empty():
            return self.cards.pop()
        else:
            return None

    def print(self):
        for card in self.cards:
            print(str(card))

    def empty(self):
        return len(self.cards) > 0

    def shuffle(self):
        random.shuffle(self.cards)

    def reset(self):
        self.__init__()
