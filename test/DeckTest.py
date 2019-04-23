import Deck
import PlayingCard

def main():

    deck = Deck.Deck()
    deck.shuffle()
    deck.reset()
    deck.print()

    card = deck.deal()
    card2 = deck.deal()

    print ()
    print (card.rank + ' ' + card.suit)
    print (card2)

if __name__ == "__main__":
    main()