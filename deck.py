from ambassador import Ambassador
from assassin import Assassin
from captain import Captain
from contessa import Contessa
from duke import Duke

class Deck:
    def __init__(self, cards_ingame, cards_outgame,cards_type)
    self.__cards_ingame = cards_ingame
    self.__cards_outgame = cards_outgame

    @property
    def cards_ingame(self):
        return self.__cards_ingame

    @property
    def cards_outgame(self):
        return self.__cards_outgame

    @cards_ingame.setter
    def cards_ingame(self, value):
        self.__cards_ingame = value

    @cards_outgame.setter
    def cards_outgame(self, value):
        self.__cards_outgame = value

    def create_deck(self):
        cards_ingame = [Ambassador, Assassin, Captain, Contessa, Duke]
        total_cards = [cards_ingame * 3]

        return total_cards

    
