# cards.py
# Authors: Jamal Almouslli, Kevin Mooney
'''

Needs:
    - a Card class with enumerable suits (faces) and ranks (values)
    - a Deck class with standard implementations of card deck behaviors, such as
        shuffling, dealing, and returning basic information such as the size of the deck.

Possibilities:
    - a Hand class that provides dynamic user management of some number of Cards.

'''

class Card:
    suits = []
    ranks = []

    suit = ''
    rank = ''

    # default to standard 52 playing card deck
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suit = suits[0]
        rank = ranks[0]

    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks
        suit = suits[0]
        rank = ranks[0]

    def random(self):
        pass

