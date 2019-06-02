import Dealer

def does_deal_work():
    dealer = Dealer.Dealer()
    cards = dealer.deal(2)
    assert len(cards) == 2

if __name__ == '__main__':
    does_deal_work()