from Player import Player
from Dealer import Dealer
from Hand import Hand
from Deck import Deck

player = Player("Kevin", 1000)
dealer = Dealer("House", 1000000)
deck = Deck()

player.draw(deck.deal(2))
player.show_hand()