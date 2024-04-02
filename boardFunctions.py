def createBoard():
    board = []
    for i in range(8):
        board.append(['*'] * 8)
    board[3][3] = 'W'
    board[3][4] = 'B'
    board[4][3] = 'B'
    board[4][4] = 'W'

    return board

def printBoard(input):
    for i in range(8):
        for j in range(8):
            print(input[i][j], end=" ")
        print()
