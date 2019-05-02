# PlayingCard.py
# Authors: Jamal Almouslli, Kevin Mooney


class PlayingCard:

    suits = {'C': "Clubs", 'H': "Hearts", 'D': "Diamonds", 'S': "Spades"}
    ranks = {1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8',
             8: '9', 9: '10', 10: 'J', 11: 'Q', 12: 'K', 13: 'A'}

    suit = None
    rank = None

    # default to standard 52 playing card deck
    def __init__(self, suit='C', rank=1):
        self.suit = suit
        self.rank = self.ranks[rank]

    def __str__(self):
        return '[' + '%2s ' % self.rank + ' of ' + self.suits[self.suit] + ']'
