import copy
import playerFunctions as pf
import monitorPlayers as mp

# heuristic: white score - black score
# white wishes to maximize, while black wishes to minimize
# in minmax we assume optimal play of either player

# in othello, we play a move which changes the scores of both characters
# this also changes the pieces on the board, and in turn, the list of playable positions
# the list of playable positions is dependent on being W or B
# we want to find the POSITION that minmaxes

def h(board):
    blackCount = 0
    whiteCount = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'W':
                whiteCount += 1
            if board[i][j] == 'B':
                blackCount += 1

    return whiteCount - blackCount


# White is the MAXIMIZER of h, Black is MINIMIZER of h

def mymax(v, bestVal):
    if v[0] > bestVal[0]:
        return v
    return bestVal


def mymin(v, bestVal):
    if v[0] < bestVal[0]:
        return v
    return bestVal


# Special max, min that decides return variable based on board evaluations

def minimax(current: pf.Player, board, depth, maximizingPlayer, alpha, beta):
    if depth == 0 or mp.stop(current, current.opp) is True:
        return h(board), None
        # Tuple of board evaluation, but no position in specific
    else:
        if maximizingPlayer:
            bestVal = float('-inf'), None
            for p in current.playable:
                tempBoard = copy.deepcopy(board)
                pf.playMove(current, tempBoard, p.x, p.y)
                current.opp.playable = mp.legalPositionList(current.opp, tempBoard)
                v = minimax(current.opp, tempBoard, depth - 1, False, alpha, beta)[0], p
                # tuple of evaluation of board on position p, position p
                bestVal = mymax(v, bestVal)
                alpha = max(alpha, bestVal[0])
                if beta <= alpha:
                    break
            return bestVal

        else:
            bestVal = float('inf'), None
            for p in current.playable:
                tempBoard = copy.deepcopy(board)
                pf.playMove(current, tempBoard, p.x, p.y)
                current.opp.playable = mp.legalPositionList(current.opp, tempBoard)
                v = minimax(current.opp, tempBoard, depth - 1, True, alpha, beta)[0], p
                bestVal = mymin(v, bestVal)
                beta = min(beta, bestVal[0])
                if beta <= alpha:
                    break
            return bestVal
