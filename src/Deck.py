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

    def deal(self, num_cards=1):
        cards_dealt = []
        if len(self.cards)>= num_cards:
            for i in range(0, num_cards):
                cards_dealt.append(self.cards.pop())
            return cards_dealt
        else:
            return None


    def print(self):
        for card in self.cards:
            print(str(card))

    def empty(self):
        return len(self.cards) == 0

    def shuffle(self):
        random.shuffle(self.cards)

    def reset(self):
        self.__init__()

    def __len__(self):
        return len(self.cards)