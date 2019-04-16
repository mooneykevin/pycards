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
        for suit in range(4):
            for rank in range(13):
                card = PlayingCard.PlayingCard(suit, rank)
                self.cards.append(card)
        # random.shuffle(cards)

    def print(self):
        for card in self.cards:
            print(str(card))

    def add(self, card):
        pass

    def draw(self):
        pass

    def shuffle(self):
        random.shuffle(self.cards)

    def clear(self):
        self.cards.clear()

    def size(self):
        return len(self.cards)

    def empty(self):
        return self.size() == 0
