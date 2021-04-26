from deck import Deck

class Player():
    def __init__(self, name, user_id, coins, alive, hand_cards):
        self.__name = name
        self.__user_id = user_id
        self.__coins = coins
        self.__alive = alive
        self.__hand_cards = hand_cards 

    @property
    def name(self):
        return self.__name

    @property
    def user_id(self):
        return self.__user_id

    @property
    def coins(self):
        return self.__coins

    @property
    def alive(self):
        return self.__alive
    
    @property
    def hand_cards(self):
        return self.__hand_cards

    @name.setter
    def name(self, value):
        self.__name = value

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    @coins.setter
    def coins(self, value):
        self.__coins = value

    @alive.setter
    def alive(self, value):
        self.__alive = value
    
    @hand_cards.setter
    def hand_cards(self, value):
        self.__hand_cards = value

    def hand()