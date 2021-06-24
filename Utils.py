# import java.text.DecimalFormat;
# import java.util.ArrayList;
# import java.util.Random;

import sys
import random
from Position import Position
from State import State
from Rook import Rook
from Knight import Knight
from Pawn import Pawn
from King import King
from Bishop import Bishop
from Queen import Queen
from Position import Position
import copy

# all the pieces
wPawn = 0
wRook = 1
wBishop = 2
wKnight = 3
wQueen = 4
wKing = 5
bPawn = 6
bRook = 7
bBishop = 8
bKnight = 9
bQueen = 10
bKing = 11
empty = 12

# number of pieces
diffPieces = 12


# name (and letter) of each piece
names = ["wPawn", "wRook", "wBishop", "wkNnight", "wQueen", "wKing", "bPawn", "bRook", "bBishop", "bkNightight",
         "bQueen", "bKing"]
letters = ["P", "R", "B", "N", "Q", "K", "p", "r", "b", "n", "q", "k", " "]
valueNames = {0:"wPawn", 1:"wRook", 2:"wBishop", 3:"wkNnight", 4:"wQueen", 5:"wKing", 6:"bPawn", 7:"bRook", 8:"bBishop", 9:"bkNight",
         10:"bQueen", 11:"bKing"}

# Note we use h for Horse instead of Knight
# Note we add " " for empty cell

# Get color piece
def getColorPiece(piece):
    if ((piece >= 0) and (piece <= 5)):
        return 0  # white
    elif ((piece > 5) and (piece <= 11)):
        return 1  # black
    else:
        print("\n** Error, wrong piece code\n")
        sys.exit(0)
    return -1  # never arrives here, just to avoid compilation error


# This method generates a problem instance.
# @param n size of the board
# @param p probability for each piece to be included
# @param seed to initiate the random generator (for reproducibility)
# @param agent the type of piece who will "play" the game (always white)
# @return the initial state (board and agent)

def getProblemInstance(n, p, seed, turn):
    numPieces = [8, 2, 2, 2, 1, 1, 8, 2, 2, 2, 1, 1]
    board = [[empty for i in range(n)] for j in range(n)]

    random.seed(seed)

    # adjusting the number of possible  pieces according to board's size
    f = (n * n) / 64.0

    for i in range(len(numPieces)):
        numPieces[i] = round(numPieces[i] * f)

    #numPieces[agent] -= 1
    allPositions = getAllBoardPositions(n)

    # placing our agent in the first row, we know these are the first n elements in allPositions
    r = random.randint(0, n - 1)
    agentPos = allPositions.pop(r)
    #board[agentPos.row][agentPos.col] = agent

    # placing the rest of pieces
    pos = None
    for piece in range(diffPieces):
        for j in range(numPieces[piece]):
            if (random.random() <= p):
                r = random.randint(0, len(allPositions) - 1)
                pos = allPositions.pop(r)
                board[pos.row][pos.col] = piece

    # Creating the instance, i.e., the state
    return State(board, turn)


#
# fill (by rows) an ArrayList with all the possible coordinates
#
# @param n size of the board
#

def getAllBoardPositions(n):
    return [Position(r, c) for r in range(n) for c in range(n)]


#
# Print a state (board + agent)
#

def printBoard(state):
    # DecimalFormat df = new DecimalFormat("00");
    size = state.m_boardSize
    # if (size>50):
    #	print("**Error, board too large to be text-printed ...\n")
    #	sys.exit(0)

    # upper row
    print("   ", end="")
    for c in range(size):
        print("% 2d " % (c), end="")
    print("")

    print("  ", end="")
    for c in range(size):
        print("---", end="")
    print("--")

    # board
    for r in range(size):
        print("% 2d|" % (r), end="")
        for c in range(size):
            print(" " + letters[state.m_board[r][c]] + "|", end="")
        # botton row
        print("  ")
        for c in range(size):
            print("---", end="")
        print("--")





def obtenerPieza(valorPieza):
        if valorPieza == wPawn:
            return Pawn(0)
        elif valorPieza == bPawn:
            return Pawn(1)
        elif valorPieza == wKnight:
            return Knight(0)
        elif valorPieza == bKnight:
            return Knight(1)
        elif valorPieza == wBishop:
            return  Bishop(0)
        elif valorPieza == bBishop:
            return Bishop(1)
        elif valorPieza == wRook:
            return Rook(0)
        elif valorPieza == bRook:
            return Rook(1)
        elif valorPieza == wQueen:
            return Queen(0)
        elif valorPieza == bQueen:
            return Queen(1)
        elif valorPieza == wKing:
            return King(0)
        elif valorPieza == bKing:
            return King(1)
        else:
            return None


def getStates(row,col,state):
    listaEstados = []
    copiaEstado = copy.deepcopy(state)
    numPieza = state.m_board[row][col]
    pieza = obtenerPieza(numPieza)
    copiaEstado.m_agentPos = Position(row, col)
    posiblesAcciones = pieza.getPossibleActions(copiaEstado)
    for action in posiblesAcciones:
        listaEstados.append(copiaEstado.applyAction(action))
    return listaEstados



def getChessInstancePosition(p, seed, turn, prof):
    numPieces = [8, 2, 2, 2, 1, 1, 8, 2, 2, 2, 1, 1]

    n = 8
    board = [[empty for i in range(n)] for j in range(n)]
    random.seed(seed)

    allPositions = getAllBoardPositions(n)
    # placing the two kings in random position
    r = random.randint(0, n*n)
    wkingPos = allPositions.pop(r)
    board[wkingPos.row][wkingPos.col] = wKing
    numPieces[wKing] -= 1
    r = random.randint(0, n*n - 1)
    bkingPos = allPositions.pop(r)
    board[bkingPos.row][bkingPos.col] = bKing

    numPieces[bKing] -=1

    pos = None
    for piece in range(diffPieces):
        for j in range(numPieces[piece]):
            if (random.random() <= p):
                r = random.randint(0, len(allPositions) - 1)
                pos = allPositions.pop(r)
                if piece == wPawn and pos.row == 7:
                    piece = wQueen
                elif piece == bPawn and pos.row == 0:
                    piece = bQueen
                board[pos.row][pos.col] = piece

    return State(board, turn, prof)



def getChessInstance(p, seed, turn, prof):
    n = 8
    board = [[empty for i in range(n)] for j in range(n)]

    random.seed(seed)

    # Number of possible pieces according to board's size
    f = 32

    for i in range(n):
        board[1][i] = wPawn
        board[n - 2][i] = bPawn

    # white pieces
    board[0][0] = wRook
    board[0][1] = wKnight
    board[0][2] = wBishop
    board[0][n - 1] = wRook
    board[0][n - 2] = wKnight
    board[0][n - 3] = wBishop
    board[0][3] = wKing
    board[0][4] = wQueen

    # black pieces

    board[n - 1][0] = bRook
    board[n - 1][1] = bKnight
    board[n - 1][2] = bBishop
    board[n - 1][n - 1] = bRook
    board[n - 1][n - 2] = bKnight
    board[n - 1][n - 3] = bBishop
    board[n - 1][3] = bKing
    board[n - 1][4] = bQueen

    # Creating the instance, i.e., the state
    state = State(board, turn, prof)
    return state


# main to test the methods

if __name__ == '__main__':
    st = getProblemInstance(8, 1.0, 1771, wRook)
    print(st.m_board)

    printBoard(st)
