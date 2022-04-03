# Creates a new board, keeps track of score and validates moves

class Board:
    def __init__(self, new):
        self.new_game = new
    
    cells = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ",9:" "}

    @classmethod
    def show_board(cls):
        for key, value in cls.cells.items():
            row = ""
            row += f"[{value}]"
            if key % 3  == 0:
                row += "\n"
            print(row, end="")

    @classmethod
    def make_move(cls, cell, symbol):
        if cell in cls.cells.keys() and cls.cells[cell] == " ":
            cls.cells[cell] = symbol
            return
        print("You can't move to that cell!")

b1 = Board(True)
b1.show_board()