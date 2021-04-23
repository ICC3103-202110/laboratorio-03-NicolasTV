from actions import Actions

class Foreign_aid:
     def __init__(self, name, action_text, check_target):
        super(Foreign_aid, self).__init__(name, action_text, check_target):
        self.name = ["Foreign Aid"]
        self.action_text = ["Gain 2 gold"]
        self.check_target = None

        def play_foreign_aid(self, players):
            players.coins += 2
            return True

    

        