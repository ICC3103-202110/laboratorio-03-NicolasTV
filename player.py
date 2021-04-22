

class Player():
    def __init__(self, name, user_id, coins):
        self.__name = name
        self.__user_id = user_id
        self.__coins = coins

    @property
    def name(self):
        return self.__name

    @property
    def user_id(self):
        return self.__user_id

    @property
    def coins(self):
        return self.__coins

    @name.setter
    def name(self, value):
        self.__name = value

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    @coins.setter
    def coins(self, value):
        self.__coins = value
