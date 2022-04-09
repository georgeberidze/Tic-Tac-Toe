# Creates a new board, keeps track of score and validates moves
import random

from players import Computer

class Board:
    def __init__(self, human_symbol, computer_symbol):
        self.cells = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ",9:" "}
        self.symbols = {"Human":human_symbol, "Computer":computer_symbol}
        self.win_combos = [{1,2,3}, {4,5,6}, {7,8,9},  # horizontal 
                           {1,4,7}, {2,5,8}, {3,6,9},  # vertical
                           {1,5,9}, {3,5,7}]           # diagonal 

    @property
    def computer_positions(self):
        return {cell[0] for cell in list(filter(lambda cell: cell[1] == self.symbols["Computer"], self.cells.items()))}
    
    @property
    def human_positions (self): 
        return {cell[0] for cell in list(filter(lambda cell: cell[1] == self.symbols["Human"], self.cells.items()))}

    def show_board(self):
        print("\n")
        for key, value in self.cells.items():
            row = ""
            row += f"[{value}]"
            if key % 3  == 0:
                row += "\n"
            print(row, end="")
        print("\n") 

    def end_game(self):
        for i in self.win_combos:
            if len(i.intersection(self.computer_positions)) == 3:
                return "You lost!"
            elif len(i.intersection(self.human_positions)) == 3:
                return "You won!"
        return False

    def make_move(self, cell, controller):
        if cell in self.cells.keys() and self.cells[cell] == " ":
            self.cells[cell] = self.symbols[controller]
            return True
        return False

    def calculate_move(self):
        win_combos = self.win_combos
        cells = self.cells
        
        neutral_options_all = [row for row in win_combos if not row.intersection(self.human_positions)] 
        neutral_options = [row.difference(self.computer_positions) for row in neutral_options_all if len(row.difference(self.computer_positions))>1] # all attack openings for computer

        defense_options = [row.difference(self.human_positions) for row in win_combos if len(row.difference(self.human_positions)) == 1 and row.difference(self.human_positions).difference(self.computer_positions)]
        attack_options = [row.difference(self.computer_positions) for row in neutral_options_all if len(row.difference(self.computer_positions))==1]

        if len(attack_options) != 0:
            return random.choice(list(map(lambda x: x.pop() if (len(x) == 1) else None, attack_options)))
        elif len(defense_options) != 0:
            return random.choice(list(map(lambda x: x.pop() if (len(x) == 1) else None, defense_options)))
        else:
            if len(self.computer_positions) == 0 and len(self.human_positions) == 0:
                return 5
            else:
                return random.choice(list(random.choice(neutral_options)))