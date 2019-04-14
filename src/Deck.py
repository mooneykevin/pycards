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
    cardType = ''

    def __init__(self, cardType='PlayingCard'):
        card = PlayingCard.PlayingCard()
        cards = card.deck()
        random.shuffle(cards)

    def print(self):
        for card in self.cards:
            print(card)

    def add(self, card):
        pass

    def draw(self):
        pass

    def reset(self):
        pass

    def shuffle(self):
        random.shuffle(self.cards)

    def clear(self):
        pass

    def size(self):
        return len(self.cards)

    def empty(self):
        pass