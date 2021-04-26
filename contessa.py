from actions import Actions


class Contessa(Actions):
    def __init__(self, name, action_text, block):
        super(Contessa, self).__init__(name, action_text, block):
        self.__name = ["Contessa"]
        self.__action_text = ["Block assasination"]
        self.__block = ["Assassin"]

    def play_contessa(self, player, target = None)
        print("Assasination bloqued")

    
    
