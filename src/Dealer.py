import Deck
import Player

class Dealer(Player):

    deck = Deck.Deck()

    def __init__(self):
        self.name = "House"
        self.money = 1000000

    def deal(self, num_cards=1):
        cards = []
        return cards