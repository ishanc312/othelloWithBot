# othelloWithBot
This is a Python implementation of the classic board game Othello. It initially begins by receiving an input from the user asking if they want to play against an AI or not.

Once the game begins, the program will continuously ask the player(s) to input a position to place a piece. Illegal moves are taken into account and the player will be asked to re-input.

The AI is based on an implementation of the Minimax Algorithm, utilizing Alpha-Beta pruning to reduce computations. A heuristic is defined in order to "evaluate" a board state.

Currently, I am working on setting up a front-end for this program to eliminate the drawback that is having to manually input positions as opposed to "clicking" on an interactive game board.
