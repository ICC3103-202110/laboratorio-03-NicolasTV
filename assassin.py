from actions import Actions
from game import Game

class Assassin(Actions):
    def __init__(self, name, action_text, block, check_target, coins_needed):
        super(Assasin, self).__init__(name, action_text, block, check_target, coins_needed):
        self.__name = ["Assassin"]
        self.__action_text = ["Pay 3 gold to remove a player`s card"]
        self.__check_target = True
        self.__coins_needed = 3

    def play_assassin(self, players, target = None):
        if players.coins < self.coins_needed:
            print("Not enough coins")

        if target == None:
            print("You must select a player")

        players.coins -=3
        target.""lose_card()""

        return True
