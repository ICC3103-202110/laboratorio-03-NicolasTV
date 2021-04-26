from actions import Actions


class Ambassador(Actions):
    def __init__(self, name, action_text, block):
        super(Ambassador, self).__init__(name, action_text, block):
        self.__name = ["Ambassador"]
        self.__action_text = ["Change this card for two more of the deck"]
        self.__block = ["Captain"]

    def play_ambassador(self, players, target = None):