from PlayingCard import PlayingCard


def test_1_default_constructor() :
    two_of_clubs = PlayingCard()
    assert two_of_clubs.suit == 'Clubs', "Error 1.1"
    assert two_of_clubs.rank == '2', "Error 1.2"


def test_2_constructor(suit, rank):
    test_card = PlayingCard(suit, rank)
    assert test_card.suit == suit, "Error 2.1"
    assert test_card.rank == rank, "Error 2.2"


def main():
    test_1_default_constructor()
    test_2_constructor('Hearts', 'Six')
    test_2_constructor('Diamonds', 'Nine')


if __name__ == "__main__":
    main()
