from Hand import Hand
from Deck import Deck


class HandTest:

    deck = Deck()
    hand = Hand()
    hand2 = Hand()

    deck.shuffle()

    # deal returns an iterable of cards, which is why we can for-loop over this call
    hand.add(deck.deal(3))

    # we can't do this, because add expects a single card and deal() now returns an iterable
    # hand2.add(deck.deal())
    # hand2.add(deck.deal(3))

    # two options:
    # 1) Always add cards to hand inside of a loop.
    # 2) Refactor the add() method to accept a List.

    print(hand)
    print(hand2)