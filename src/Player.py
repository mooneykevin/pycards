from Hand import Hand

class Player:

    name = None
    _hand = None
    money = 0

    def __init__(self, name="Unknown", money=0):
        self.name = name
        self.money = money
        self._hand = Hand()

    def draw(self, cards):
        self._hand.add(cards)

    def discard(self, card):
        self.hand.remove(card)

    def show_hand(self):
        pass


    def __str__(self):
        return "{} has ${}".format(self.name, self.money)