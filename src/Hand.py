class Hand:

    hand = []

    def __init__(self):
        self.hand = []

    def add(self, cards):
        for card in cards:
            self.hand.append(card)

    # this is O(n^2) but we'll take it for now since n < 53
    def remove(self, card):
        for c in self.hand:
            if str(c) == str(card):
                self.hand = [i for i in self.hand if not(i == card)]

    # works because our PlayingCard class has a __str__ method defined
    def __str__(self):
        cardstrings = []
        for card in self.hand:
            cardstrings.append(str(card))
        return ' '.join(cardstrings)

    def contains(self, card):
        return self.__contains__(card)

    def __contains__(self, item):
        for card in self.hand:
            if item.suit == card.suit and item.rank == card.rank:
                return True
        return False

    def size(self):
        return len(self)

    def __len__(self):
        return len(self.hand)

