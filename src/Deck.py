# Deck.py
# Authors: Jamal Almouslli, Kevin Mooney
'''

Needs:
    - a Card class with enumerable suits (faces) and ranks (values)
    - a Deck class with standard implementations of card deck behaviors, such as
        shuffling, dealing, and returning basic information such as the size of the deck.

Possibilities:
    - a Hand class that provides dynamic user management of some number of Cards.

'''

import PlayingCard
import random

class Deck:

    cards = []
    card_type = ''

    def __init__(self, card_type='PlayingCard'):
        self.cards = []
        for suit in ['C', 'H', 'D', 'S']:
            for rank in range(1,14):
                card = PlayingCard.PlayingCard(suit, rank)
                self.cards.append(card)

    def deal(self):
        if self.isNotEmpty():
            return self.cards.pop()
        else:
            return None

    def print(self):
        for card in self.cards:
            print(str(card))

    def isNotEmpty(self):
        return len(self.cards) > 0

    def shuffle(self):
        random.shuffle(self.cards)

    def reset(self):
        self.__init__()
