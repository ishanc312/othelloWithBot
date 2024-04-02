class Player:
    name = None
    color = None
    coins = 30
    score = 2
    playable = None
    opp = None
    playAsBot = False
    strategy = None

    def __init__(self, n, c, strat):
        self.name = n
        self.color = c
        self.strategy = strat

    def getOppColor(self):
        if self.color == 'W':
            return 'B'
        else:
            return 'W'

    def alterScore(self, flip):
        self.coins -= 1
        self.score = self.score + flip + 1
        self.opp.score -= flip


class Pos:
    x = None
    y = None

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __add__(self, other):
        out = Pos(self.x + other.x, self.y + other.y)
        return out

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


UP, DOWN = Pos(-1, 0), Pos(1, 0)
LEFT, RIGHT = Pos(0, -1), Pos(0, 1)

DIRECTIONS = [UP, UP + RIGHT, RIGHT, DOWN + RIGHT, DOWN, DOWN + LEFT, LEFT, UP + LEFT]

# --------------------------------------

def getBracket(player: Player, board, m, n, d: Pos):
    deltaY = d.x
    deltaX = d.y
    inc = 1
    opp = player.getOppColor()

    try:
        while board[m + inc * deltaY][n + inc * deltaX] == opp:
            inc += 1
        # keep travelling in direction if we find black
    except IndexError:
        return None
        # we go out of bounds, no bracket found
    if board[m + inc * deltaY][n + inc * deltaX] == '*' or inc == 1:
        return None
        # break if we run into a star
        # or increment is 1, meaning we immediately found a star or our own color
    else:
        out = Pos(m + inc * deltaY, n + inc * deltaX)
        return out
    # if there are any possible brackets it is a legal move


def playMove(player: Player, board, m, n):
    flippedCoins = 0
    color = player.color

    for d in DIRECTIONS:
        deltaY = d.x
        deltaX = d.y
        bracket = getBracket(player, board, m, n, d)
        if bracket is not None:
            inc = 1
            while board[m + inc * deltaY][n + inc * deltaX] != color:
                board[m + inc * deltaY][n + inc * deltaX] = color
                inc += 1
                # make the flips on our board
            board[m][n] = color  # place piece at our position
            flippedCoins = flippedCoins + inc - 1
            # subtract the over count by 1

    return flippedCoins
    # output will be put into the alterScore function
    # we calculate flippedCoins and alter board, but we don't alter the score


def isLegalMove(player: Player, board, m, n):
    bracketsFound = 0
    if board[m][n] == "*":
        for d in DIRECTIONS:
            bracket = getBracket(player, board, m, n, d)
            if bracket is not None:
                bracketsFound += 1
        if bracketsFound > 0:
            return True
    return False
    # return False is position is filled or no brackets found
    # return True if we find at least 1 bracket
