from actions import Actions


class Ambassador(Actions):
    def __init__(self, name, action_text, block):
        super(Ambassador, self).__init__(name, action_text, block):
        name = ["Ambassador"]
        action_text = ["Change this card for two more of the deck"]
        block = ["Captain"]

    def play_ambassador(self, players, target = None):