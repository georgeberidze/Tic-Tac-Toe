
import board
import random

class Player:
    def __init__(self):
        self.score = 0

class Human(Player):
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
