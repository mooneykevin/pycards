# Deck.py
# Authors: Jamal Almouslli, Kevin Mooney

import PlayingCard
import random


class Deck:

    deck = []
    card_type = ''

    def __init__(self):
        self.deck = []
        for suit in ['C', 'H', 'D', 'S']:
            for rank in range(1, 14):
                card = PlayingCard.PlayingCard(suit, rank)
                self.deck.append(card)
        self.shuffle()

    def deal(self, num_cards=1):
        cards_dealt = []
        if len(self.deck) >= num_cards:
            for i in range(0, num_cards):
                cards_dealt.append(self.deck.pop())
            return cards_dealt
        else:
            return None


    def print(self):
        for card in self.deck:
            print(str(card))

    def empty(self):
        return len(self.deck) == 0

    def shuffle(self):
        random.shuffle(self.deck)

    def reset(self):
        self.__init__()

    def __len__(self):
        return len(self.deck)