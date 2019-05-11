from Player import Player
from Hand import Hand
from Deck import Deck


class PlayerTest:

    deck = Deck()
    deck.shuffle()

    player = Player("Jamal", Hand(), 1000)
    player.draw(deck.deal(5))
    print(player.name)
    print()
    print(player._hand)
    print()
    print(player.money)
