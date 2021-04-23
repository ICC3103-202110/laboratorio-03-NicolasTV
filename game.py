from actions import Actions
from coup import Coup
from income import Income
from foreign_aid import Foreign_aid
from ambassador import Ambassador
from assassin import Assassin
from captain import Captain
from contessa import Contessa
import random


class Game():

    COUP_COINS = 7

    def __init__(self, cards_type, general_actions,
                 cards_ingame, cards_outgame, deck,
                 players_playing):
        self.__cards_type = cards_type
        self.__general_actions = general_actions
        self.__cards_ingame = cards_ingame
        self.__cards_outgame = cards_outgame
        self.__deck = deck
        self.__players_playing = players_playing

    @property
    def cards_type(self):
        return self.__cards_type

    @property
    def general_actions(self):
        return self.__general_actions

    @property
    def cards_ingame(self):
        return self.__cards_ingame

    @property
    def cards_outgame(self):
        return self.__cards_outgame

    @property
    def deck(self):
        return self.__deck

    @property
    def players_playing(self):
        return self.__players_playing

    @cards_type.setter
    def cards_type(self, value):
        self.__cards_type = value

    @general_actions.setter
    def general_actions(self, value):
        self.__general_actions = value

    @cards_ingame.setter
    def cards_ingame(self, value):
        self.__cards_ingame = value

    @cards_outgame.setter
    def cards_outgame(self, value):
        self.__cards_outgame = value

    @deck.setter
    def deck(self, value):
        self.__deck = value

    @players_playing.setter
    def players_playing(self, value):
        self.__players_playing = value

    def create_deck(self, cards_type):
        cards_type = [Actions.Duke, Actions.Captain,
                    Actions.Ambassador, Actions.Contessa, Actions.Assassin]
        
        deck = cards_type * 3

        random.shuffle(deck)

        return deck
