



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

    def calculate_move(cells):
        pass


win_combos = [{1,2,3}, {4,5,6}, {7,8,9},  # horizontal 
              {1,4,7}, {2,5,8}, {3,6,9},  # vertical
              {1,5,9}, {3,5,7}]           # diagonal

cells = {1:" ", 2:" ", 3:" ", 
         4:" ", 5:" ", 6:" ", 
         7:" ", 8:" ", 9:" "}

key_values = list(cells.items())

computer_positions = {cell[0] for cell in list(filter(lambda cell: cell[1] == "0", key_values))}
human_positions = {cell[0] for cell in list(filter(lambda cell: cell[1] == "X", key_values))}

defense_options = [row.difference(human_positions) for row in win_combos if len(row.difference(human_positions)) == 1 and row.difference(human_positions).difference(computer_positions)]
neutral_options_all = [row for row in win_combos if not row.intersection(human_positions)] 

#attack_options = [row.difference(computer_positions) for row in win_combos if len(row.difference(computer_positions)) == 1 and row.difference(computer_positions).difference(human_positions)]  # fewer options = higher priority

neutral_options = [row.difference(computer_positions) for row in neutral_options_all if len(row.difference(computer_positions))>1] # all attack openings for computer
attack_options = [row.difference(computer_positions) for row in neutral_options_all if len(row.difference(computer_positions))==1]
#print(neutral_options)

#print(test1, "**", computer_positions)
#print(human_positions, "*****", win_combos)
#for i in test1:
#    print(i.difference(computer_positions))

#print(neutral_options_all)

print(f"Attack: {attack_options}\nDefend: {defense_options}\nNeutral: {neutral_options}")
