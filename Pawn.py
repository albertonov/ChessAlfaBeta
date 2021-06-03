import Utils
from Position import Position
from Piece import Piece
from Action import Action


# this class implements the getPossibleActions for each type of piece

class Pawn(Piece):

    # constructor
    def __init__(self, color):
        self.m_color = color

        if color == 0:
            self.m_type = Utils.wPawn
        else:
            self.m_type = Utils.bPawn

    # this method must be completed with all the possible pieces
    def getPossibleActions(self, state):

        r = state.m_agentPos.row
        c = state.m_agentPos.col
        action = None

        l = []

        oponent_color = -1
        if self.m_color == 0:  # white pawn
            oponent_color = 1
            if r <= 6:
                if state.m_board[r + 1][c] == Utils.empty:  # standard pawn move
                    l.append(Action(state.m_agentPos, Position(r + 1, c)))
                if r == 1 and (state.m_board[r + 2][c] == Utils.empty):  # starting pawn move
                    l.append(Action(state.m_agentPos, Position(r + 2, c)))

                if c > 0 and (state.m_board[r + 1][c - 1] != Utils.empty) and (
                        Utils.getColorPiece(state.m_board[r + 1][c - 1]) == oponent_color):  # capture
                    l.append(Action(state.m_agentPos, Position(r + 1, c - 1)))
                if c < (state.m_boardSize - 1) and (state.m_board[r + 1][c + 1] != Utils.empty) and (
                        Utils.getColorPiece(state.m_board[r + 1][c + 1]) == oponent_color):  # capture
                    l.append(Action(state.m_agentPos, Position(r + 1, c + 1)))


        elif self.m_color == 1:  # black pawn
            oponent_color = 0
            if r >=1:
                if state.m_board[r - 1][c] == Utils.empty:  # standard pawn move
                    l.append(Action(state.m_agentPos, Position(r - 1, c)))
                if r == 6 and (state.m_board[r - 2][c] == Utils.empty):  # starting pawn move
                    l.append(Action(state.m_agentPos, Position(r - 2, c)))

                if c > 0 and (state.m_board[r - 1][c - 1] != Utils.empty) and (
                        Utils.getColorPiece(state.m_board[r - 1][c - 1]) == oponent_color):  # capture
                    l.append(Action(state.m_agentPos, Position(r - 1, c - 1)))

                if c < (state.m_boardSize - 1) and (state.m_board[r - 1][c + 1] != Utils.empty) and (
                        Utils.getColorPiece(state.m_board[r - 1][c + 1]) == oponent_color):  # capture
                    l.append(Action(state.m_agentPos, Position(r - 1, c + 1)))


        return l