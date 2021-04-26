from actions import Actions


class Duke(Actions):
    def __init__(self, name, action_text, block):
        super(Duke, self).__init__(name, action_text, block):
        self.__name = ["Duke"]
        self.__action_text = ["Block Foreign Aid and Gain 3 gold"]
        self.__block = ["Foreign Aid"]

    def play_duke(self, players, target=None):
        players.coins += 3

        return True
