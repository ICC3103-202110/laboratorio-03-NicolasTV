from actions import Actions


class Captain(Actions):
    def __init__(self, name, action_text, block, check_target):
        super(Captain, self).__init__(name, action_text, block, check_target):
        name = ["Captain"]
        action_text = ["Steal 2 gold from a selected player or block a steal"]
        block = ["Captain"]
        check_target = True

    def play_captain(self, players, target = None):
        steal = 0

        if target == None:
            print("You need to select a player")

        if target.coins >= 2:
            steal = 2
        elif target.coins == 1:
            steal = 1

        target.coins -= steal
        if target.coins < 0:
            target.coins = 0
            players.coins += steal

        return True
