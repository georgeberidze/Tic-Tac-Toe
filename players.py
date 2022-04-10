'''
Player parent class is responsible for instantiating humans and computers
'''

class Player:
    'Right now this parent class is empty but this OOP structure makes it easier to add more variables down the line if needed'
    def __init__(self):
        pass

class Human(Player):
    'This is a class controller by the human player. Computer child class is created automatically'
    def __init__(self, symbol):
        super().__init__()
        self.symbol = symbol
        if self.symbol == "X":
            self.computer = Computer("0")       
        else:
            self.computer = Computer("X")

class Computer(Player):
    def __init__(self, symbol):
        super().__init__()
        self.symbol = symbol
