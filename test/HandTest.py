from Hand import Hand
from Deck import Deck


class HandTest:

    deck = Deck()
    hand = Hand()
    hand2 = Hand()

    # Should add A and King of Spades to hand
    aceOfSpades = deck.deal()
    kingOfSpades = deck.deal()

    hand.add(aceOfSpades)
    hand.add(kingOfSpades)

    # should print Yes if the second add is performed, else No
    if hand.__contains__(kingOfSpades):
        print("Yes1")
    else:
        print("No1")

    print("hand1: ")
    hand.display()
    print()

    # test with random cards
    deck2 = Deck()
    deck2.shuffle()

    card1 = deck2.deal()
    card2 = deck2.deal()

    hand2.add(card1)
    # hand2.add(card2)

    if hand2.contains(card2):
      print("Yes2")
    else:
       print("No2")

    print("hand2: ")
    hand2.display()
    print()

    # test remove
    hand2.remove(card1)
    print("hand2: ")
    hand2.display()

