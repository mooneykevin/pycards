from Hand import Hand
from Deck import Deck


class HandTest:

    deck = Deck()

    deck.shuffle()

    hand = Hand()
    hand.add(deck.deal(-1))

    hand2 = Hand()
    hand2.add(deck.deal(0))

    hand3 = Hand()
    hand3.add(deck.deal())

    hand4 = Hand()
    hand4.add(deck.deal(1))

    hand5 = Hand()
    hand5.add(deck.deal(5))

    # should print nothing
    print("\nfirst hand:\n")
    print(hand)

    # should also print nothing
    print("\nsecond hand:\n")
    print(hand2)

    # should just print 1 card
    print("\nthird hand:\n")
    print(hand3)

    # should also just print 1 card
    print("\nfourth hand:\n")
    print(hand4)

    print("\nfifth hand:\n")
    print(hand5)
