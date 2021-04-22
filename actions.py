
class Actions():
    def __init__(self, name, action_text, check_target,
                 coins_needed, block):
        self.__name = name
        self.__action_text = action_text
        self.__check_target = check_target
        self.__coins_needed = coins_needed
        self.__block = block

    @property
    def name(self):
        return self.__name

    @property
    def action_text(self):
        return self.__action_text

    @property
    def check_target(self):
        return self.__check_target

    @property
    def coins_needed(self):
        return self.__coins_needed

    @property
    def block(self):
        return self.__block

    @name.setter
    def name(self, value):
        self.__name = value

    @action_text.setter
    def action_text(self, value):
        self.__action_text = value

    @check_target.setter
    def check_target(self, value):
        self.__check_target = value

    @block.setter
    def block(self, value):
        self.__block = value
