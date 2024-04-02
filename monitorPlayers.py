import playerFunctions as pf

def legalPositionList(player: pf.Player, board):
    playable = []
    for i in range(8):
        for j in range(8):
            if pf.isLegalMove(player, board, i, j):
                playable.append(pf.Pos(i, j))
    return playable
    # creates a list of Pos

def existsMove(playable):
    if len(playable) == 0:
        return False
    return True
    # if its empty or of size 0 that means there are no valid moves


def stop(one: pf.Player, two: pf.Player):
    if len(one.playable) == 0 and len(two.playable) == 0:
        return True
    return False
