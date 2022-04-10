# Tic-Tac-Toe - Python Console Game

## How to play
Simply run ```main.py``` and follow in-game directions

## Screenshot
<img src="/screenshot.png" width="600">

## Computer algorithm
Computer is focused on winning in least possible moves. Its decision making follows 4 steps (decreasing priority):
1. (Attack) Try to win in 1 move
2. (Defend) Prevent opponent from winning in 1 move
3. (Neutral move) If 2 and 3 don't work, move to a neutral cell and start building a winning combo -> random move
4. (Draw) If there is no way to build a winning combo, make it a draw -> random move

To make the game more interesting, there is a possibilty that computer makes mistakes for 2 reasons:
1. There are ways to win Tic-Tac-Toe 100% percent but the computer is not going to block such moves -> the computer does not plan moves ahead
2. Neutral moves (that don't lead to win or loss in 1 move) are random  

## Why I made this
My main goal was to practice the following Python concepts:
- @property decorators
- OOP (Inheritance)
- List/Set/Dictionary comprehension
- Map and Filter functions
- Lambdas
- Random library
- Set operations

## License
[MIT](https://choosealicense.com/licenses/mit/)