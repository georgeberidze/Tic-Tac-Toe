import board 
import players

game_logo = """
==================================================================================
████████ ██  ██████       ████████  █████   ██████       ████████  ██████  ███████ 
   ██    ██ ██               ██    ██   ██ ██               ██    ██    ██ ██      
   ██    ██ ██      █████    ██    ███████ ██      █████    ██    ██    ██ █████   
   ██    ██ ██               ██    ██   ██ ██               ██    ██    ██ ██      
   ██    ██  ██████          ██    ██   ██  ██████          ██     ██████  ███████
==================================================================================                                                                                                                  
"""
h1 = players.Human("X")

b1 = board.Board(h1.symbol, h1.computer.symbol)
b1.make_move(4, "Human")
b1.make_move(b1.calculate_move(),"Computer")
print(b1.computer_positions)
b1.show_board()
b1.make_move(3, "Human")
b1.make_move(b1.calculate_move(),"Computer")
print(b1.computer_positions)
b1.show_board()