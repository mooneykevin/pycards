class Player:

    name = None
    _hand = None
    money = 0

    def __init__(self, name, hand, money):
        self.name = name
        self._hand = hand
        self.money = money

    def draw(self, cards):
        self._hand.add(cards)

    def discard(self, card):
        self.hand.remove(card)


    def __str__(self):
        return "{} has ${}".format(self.name, self.money)