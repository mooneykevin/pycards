from Hand import Hand


class Player:

    name = None
    hand = Hand()

    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def print_name(self):
        print(self.name)
