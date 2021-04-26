from actions import Actions
from player import Player


class Income(Actions):
    def __init__(self, name, action_text, check_target):
        super(Income, self).__init__(name, action_text, check_target)
        self.__name = "Income"
        self.__action_text = "Gain 1 gold"
        self.__check_target = None

    def play_income(self, players):
        players.coins += 1

        return True
