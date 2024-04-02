import boardFunctions as bf
import playerFunctions as pf
import monitorPlayers as mp
import oBot as ob

print("WELCOME TO OTHELLO!")
print()
board = bf.createBoard()
bf.printBoard(board)
print()

p1 = pf.Player("Player 1", 'B', False)
p2 = pf.Player("Player 2", 'W', True)
p1.playable = mp.legalPositionList(p1, board)
p2.playable = mp.legalPositionList(p2, board)
# initialize their list of playable moves
p1.opp = p2
p2.opp = p1
# set eachother as the opponent
turn = 1
# turn/round # begins at 1

# ------------------------------

def currentPlayer():
    if turn % 2 == 1:
        return p1
    else:
        return p2

def outcome():
    print("GAME OVER!")
    if p1.score > p2.score:
        print("Player 1 wins!")
    elif p1.score < p2.score:
        print("Player 2 wins!")
    else:
        print("Draw.")

# -------------------------------------------------------------

choice = input("Would you like to play against a bot today? Please enter Y if Yes: ")
if choice == 'Y':
    p2.playAsBot = True

# -------------------------------------------------------------

# MAIN WHILE LOOP DRIVER
while not mp.stop(p1, p2):
    current = currentPlayer()
    # define the current player for our usage
    if mp.existsMove(current.playable):
        i, j = None, None
        if current.playAsBot:
            posChoice = ob.minimax(current, board, 3, current.strategy, float('-inf'), float('inf'))[1]
            # utilize minmax to calculate optimal position to play
            # note bot is white, so it is maximizing player
            i = posChoice.x
            j = posChoice.y
        else:
            i, j = map(int, input(f"{current.name}, please enter in a position to place a piece: ").split())
            while pf.Pos(i, j) not in current.playable:
                i, j = map(int, input(f"{current.name}, please enter in a VALID position: ").split())
                # forces user to input valid position by checking if its in the playable

        current.alterScore(pf.playMove(current, board, i, j))
        # play the move, alter the scores
        print(f"{current.name} places " + current.color + f" at the position {i, j}.")

        turn += 1
        print()
    else:
        # skip and forfeit their turn
        turn += 1
        print(f"{current.name} has no possible moves.")
        print()

    current.opp.playable = mp.legalPositionList(current.opp, board)
    # current turn is over; opponent who's turn is next now has a new list of playable positions

    bf.printBoard(board)
    print(f"Player 1: {p1.score}" + f" | Player 2: {p2.score}")
    print()

outcome()
# simple function for outputting the winner
