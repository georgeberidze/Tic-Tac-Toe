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

print(f"{game_logo}\nHello, this is a classic Tic-Tac-Toe game. You are going to play against a computer.\nEach cell has a number from 1 to 9. Like this:\n")
print('''
   [1][2][3]
   [4][5][6]
   [7][8][9]
   \n''')

quit = False

while True:
   print("> Choose 'X' or '0' to start: ", end="")
   try:
      player_choice = input()
      assert player_choice in ["X", "0"]
      break
   except:
      print("invalid input!")
      continue

human = players.Human(player_choice)
board = board.Board(player_choice,human.computer.symbol)
board.show_board()

while board.end_game() == False:
   print("It's your turn. Choose a valid cell: ", end="")
   try:
      player_move = int(input())
      if board.end_game() != False:
         break
      assert board.make_move(player_move, "Human") == True
      print(f"You moved to cell {player_move}")
      board.show_board()
      if board.end_game() != False:
         break
      print("Computer made the move")
      board.make_move(board.calculate_move(), "Computer")
      board.show_board()
      #print(f"Computer moved to {board.calculate_move()}")
   except:
      print("Invalid cell!")
      pass

print(board.end_game())
