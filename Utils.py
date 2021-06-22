import sys
import random
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
valueNames = {0: "wPawn", 1: "wRook", 2: "wBishop", 3: "wkNnight", 4: "wQueen", 5: "wKing", 6: "bPawn", 7: "bRook",
              8: "bBishop", 9: "bkNightight",
              10: "bQueen", 11: "bKing"}


# Note we use h for Horse instead of Knight
# Note we add " " for empty cell

# Get color piece
def get_color_piece(piece):
    if (piece >= 0) and (piece <= 5):
        return 0  # white
    elif (piece > 5) and (piece <= 11):
        return 1  # black
    else:
        print("\n** Error, wrong piece code\n")
        sys.exit(0)
    return -1  # never arrives here, just to avoid compilation error


# fill (by rows) an ArrayList with all the possible coordinates
#
# @param n size of the board
#

def get_all_board_positions(n):
    return [Position(r, c) for r in range(n) for c in range(n)]


#
# Print a state (board + agent)
#

def print_board(state):
    size = state.m_boardSize
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
        # bottom row
        print("  ")
        for c in range(size):
            print("---", end="")
        print("--")


def get_states(x, y, state):
    state_list = []
    value = state.m_board[x][y]
    piece = piece_factory(value)
    mod_state = copy.deepcopy(state)  # state hard copy, ready to be modified
    mod_state.m_agentPos = Position(x, y)
    actions = piece.get_possible_actions(mod_state)
    for each in actions:
        state_list.append(mod_state.applyAction(each))  # makes its own copy
    return state_list


def piece_factory(value):
    if value == wPawn:
        return Pawn(0)
    elif value == bPawn:
        return Pawn(1)
    elif value == wRook:
        return Rook(0)
    elif value == bRook:
        return Rook(1)
    elif value == wKing:
        return King(0)
    elif value == bKing:
        return King(1)
    elif value == wQueen:
        return Queen(0)
    elif value == bQueen:
        return Queen(1)
    elif value == wBishop:
        return Bishop(0)
    elif value == bBishop:
        return Bishop(1)
    elif value == wKnight:
        return Knight(0)
    elif value == bKnight:
        return Knight(1)
    else:
        return None


def get_chess_instance_position(p, seed, turn):
    num_pieces = [8, 2, 2, 2, 1, 1, 8, 2, 2, 2, 1, 1]

    n = 8
    board = [[empty for i in range(n)] for j in range(n)]
    random.seed(seed)

    all_positions = get_all_board_positions(n)
    # placing the two kings in random position
    r = random.randint(0, n * n)
    w_king_pos = all_positions.pop(r)
    board[w_king_pos.row][w_king_pos.col] = wKing
    num_pieces[wKing] -= 1
    r = random.randint(0, n * n - 1)
    b_king_pos = all_positions.pop(r)
    board[b_king_pos.row][b_king_pos.col] = bKing
    num_pieces[bKing] -= 1

    for piece in range(diffPieces):
        for j in range(num_pieces[piece]):
            if random.random() <= p:
                r = random.randint(0, len(all_positions) - 1)
                pos = all_positions.pop(r)
                # promote any piece to Queen if spawned on opposite side
                if piece == wPawn and pos.row == 7:
                    piece = wQueen
                elif piece == bPawn and pos.row == 0:
                    piece = bQueen
                board[pos.row][pos.col] = piece
    return State(board, turn)


def get_chess_instance(p, seed, turn):
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
    state = State(board, turn)
    return state
