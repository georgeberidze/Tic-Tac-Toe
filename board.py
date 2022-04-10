'''
board class is responsible for creating and showing 3x3x3 board, validating moves, computer AI moves and deciding when the game ends and how
'''
import random

class Board:
    def __init__(self, human_symbol, computer_symbol):
        self.cells = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ",9:" "}     # this dictionary shows the current state of the game
        self.symbols = {"Human":human_symbol, "Computer":computer_symbol}
        self.win_combos = [{1,2,3}, {4,5,6}, {7,8,9},       # these are all possible ways you can win at Tic-Tac-Toe
                           {1,4,7}, {2,5,8}, {3,6,9},  
                           {1,5,9}, {3,5,7}]           

    @property       
    def computer_positions(self):
        'Returns A SET of all cells where the computer has made moves'
        return {cell[0] for cell in list(filter(lambda cell: cell[1] == self.symbols["Computer"], self.cells.items()))}
    
    @property
    def human_positions (self): 
        'Returns A SET of all cells where the human player has made moves'
        return {cell[0] for cell in list(filter(lambda cell: cell[1] == self.symbols["Human"], self.cells.items()))}

    @property
    def empty_positions (self): 
        'Returns A SET of all cells that are empty'
        return {cell[0] for cell in list(filter(lambda cell: cell[1] == " ", self.cells.items()))}

    def show_board(self):
        'Displayes 3x3x3 board in its current state'
        print("\n")
        for key, value in self.cells.items():
            row = ""
            row += f"[{value}]"
            if key % 3  == 0:
                row += "\n"
            print(row, end="")

    def end_game(self):
        'Returns False if the game has not yet ended'
        if len(self.empty_positions) == 0:
            return "It's a draw!"
        for i in self.win_combos:
            if len(i.intersection(self.computer_positions)) == 3:
                return "You lost!"
            elif len(i.intersection(self.human_positions)) == 3:
                return "You won!"
        return False

    def make_move(self, cell, controller):
        'Validates the move that the computer or human is trying to make and updates a corresponding cell'
        if cell in self.cells.keys() and self.cells[cell] == " ":
            self.cells[cell] = self.symbols[controller]
            return True
        return False

    def calculate_move(self):
        '''
        Main algorithm that decides how computer should make the move. Computer is focused on winning in least possible moves. The decision making follows 4 steps:
            1. Try to win in 1 move
            2. Prevent opponent from winning in 1 move
            3. If 2 and 3 don't work, move to a neutral cell and start building a winning combo -> random move
            4. If there is no way to build a winning combo, make it a draw -> random move
        
        To make the game more interesting, there is a possibilty that computer makes mistakes for 2 reasons:
            1. There are ways to win Tic-Tac-Toe 100% percent but the computer is not going to block such moves -> the computer does not plan moves ahead
            2. Neutral moves (that don't lead to win or loss in 1 move) are random  
        '''
        win_combos = self.win_combos
        
        neutral_options_all = [row for row in win_combos if not row.intersection(self.human_positions)]
        neutral_options = [row.difference(self.computer_positions) for row in neutral_options_all if len(row.difference(self.computer_positions))>1]

        defense_options = [row.difference(self.human_positions) for row in win_combos if len(row.difference(self.human_positions)) == 1 and row.difference(self.human_positions).difference(self.computer_positions)]
        attack_options = [row.difference(self.computer_positions) for row in neutral_options_all if len(row.difference(self.computer_positions))==1]

        if len(attack_options) != 0:
            'There is an opportunity to win in 1 move'
            return random.choice(list(map(lambda x: x.pop() if (len(x) == 1) else None, attack_options)))
        elif len(defense_options) != 0:
            'Defense is needed otherwise opponent wins'
            return random.choice(list(map(lambda x: x.pop() if (len(x) == 1) else None, defense_options)))
        elif len(neutral_options) != 0:
            'Move to an empty cell which has a chance to build a winning combo'
            return random.choice(list(random.choice(neutral_options)))
        else:
            'Move to a random empty cell -> leads to a draw'
            return random.choice(list(self.empty_positions))