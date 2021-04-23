from actions import Actions
from player import Player


class Coup(Actions):
    def __init__(self, name, action_text, check_target,
                 coins_needed):
        super(Coup, self).__init__(name, action_text, check_target, coins_needed)
        name = ["Coup"]
        action_text = ["Pay 7 gold to remove a card from a selected player."]
        check_target = True
        coins_needed = 7

    

