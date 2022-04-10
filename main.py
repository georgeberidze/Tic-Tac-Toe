'''
Game runs from this file. 
'''

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
   ''')

while True:
   'Game loop. Runs until user quits the game.'

   while True:
      'Input validation loop. Runs until a valid symbol is chosen.'
      print("\n> Choose 'X' or '0' to start the game: ", end="")
      try:
         player_choice = input()
         assert player_choice in ["X", "0"]     # Throw exception if this condition is not met
         print(f"\nYou are playing as {player_choice}")
         break
      except:
         print("\nTry again! You can only choose 'X' or '0'\n")
         continue    # restart the inner loop

   ## Instantiate players and the game board
   human = players.Human(player_choice)      
   b1 = board.Board(human.symbol,human.computer.symbol)
   b1.show_board()

   while b1.end_game() == False:
      'Loop for taking turns. Runs until game ends in a win or a draw.'
      print("\n> It's your turn. Choose a valid cell: ", end="")
      try:
         'Move validation'
         player_move = int(input())
         if b1.end_game() != False:
            'If the game ends, break the loop'
            break
         assert b1.make_move(player_move, "Human") == True     # throw an exception is the move is not valid
         print(f"\nYou moved to cell {player_move}")
         b1.show_board()
         if b1.end_game() != False:
            break
         b1.make_move(b1.calculate_move(), "Computer")
         print("\nComputer made the move")
         b1.show_board()
      except:
         'Move is not valid'
         print("\nThat's not a valid move. Try again!")
         pass

   print("\n",b1.end_game(), end="\n")

   user_replay = input("\n> Press any key to restart the game. Type 'Q' to quit.")
   if user_replay == "Q":
      break

print("\nGoodbye!\n")