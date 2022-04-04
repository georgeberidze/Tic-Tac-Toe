# Creates a new board, keeps track of score and validates moves

class Board:
    def __init__(self):
        self.cells = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ",9:" "}
        self.symbols = ("X", "0")

    def show_board(self):
        for key, value in self.cells.items():
            row = ""
            row += f"[{value}]"
            if key % 3  == 0:
                row += "\n"
            print(row, end="")

    def make_move(self, cell, controller):
        if cell in self.cells.keys() and self.cells[cell] == " ":
            self.cells[cell] = controller.symbol
            return
        print("You can't move to that cell!")
