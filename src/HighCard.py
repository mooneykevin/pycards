from Deck import Deck
from Player import Player
from Hand import Hand

def game():

    # initialization
    players = []
    rounds = 1

    for i in range(0, int(input("how many players? "))):
        name = input('Player {} name: '.format(i+1))
        money = int(input('Player {} money: '.format(i+1)))
        while money <= 0:
            money = str(input('Enter a value greater than 0: '))
        players.append(Player(name, Hand(), money))

    rounds = int(input('How many rounds do you want to play? '))

    # main game loop
    for i in range(0, rounds):

        # betting phase
        bets = []
        for i in range(0, len(players)):
            bet = int(input('{} has ${}. How much will {} bet? $'.format(players[i].name, players[i].money, players[i].name)))
            while bet >= players[i].money or bet < 0:
                bet = int(input('Not allowed. Current balance: ${}. Please bet again: $'.format(players[i].money)))
            players[i].money -= bet
            bets.append(bet)

        # deal phase
        # eval phase








if(__name__ == '__main__'):
    game()