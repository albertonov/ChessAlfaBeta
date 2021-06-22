import Utils
from Position import Position
from Piece import Piece
from Action import Action


class Pawn(Piece):

    def __init__(self, color):
        self.m_color = color

        if color == 0:
            self.m_type = Utils.wPawn
        else:
            self.m_type = Utils.bPawn

    def get_possible_actions(self, state):

        r = state.m_agentPos.row
        c = state.m_agentPos.col
        l = []

        if self.m_color == 0:  # white
            if r <= 6:
                if state.m_board[r + 1][c] == Utils.empty:  # standard move, empty
                    l.append(Action(state.m_agentPos, Position(r + 1, c)))
                if r == 1 and (state.m_board[r + 2][c] == Utils.empty) and (
                        state.m_board[r + 1][c] == Utils.empty):  # starting move, empty
                    l.append(Action(state.m_agentPos, Position(r + 2, c)))

                if c > 0 and (state.m_board[r + 1][c - 1] != Utils.empty) and (
                        Utils.get_color_piece(state.m_board[r + 1][c - 1]) != self.m_color):  # capture
                    l.append(Action(state.m_agentPos, Position(r + 1, c - 1)))
                if c < (state.m_boardSize - 1) and (state.m_board[r + 1][c + 1] != Utils.empty) and (
                        Utils.get_color_piece(state.m_board[r + 1][c + 1]) != self.m_color):  # capture
                    l.append(Action(state.m_agentPos, Position(r + 1, c + 1)))

        elif self.m_color == 1:  # black
            if r >= 1:
                if state.m_board[r - 1][c] == Utils.empty:  # standard move, capture
                    l.append(Action(state.m_agentPos, Position(r - 1, c)))
                if r == 6 and (state.m_board[r - 2][c] == Utils.empty) and (
                        state.m_board[r - 1][c] == Utils.empty):  # starting move, capture
                    l.append(Action(state.m_agentPos, Position(r - 2, c)))

                if c > 0 and (state.m_board[r - 1][c - 1] != Utils.empty) and (
                        Utils.get_color_piece(state.m_board[r - 1][c - 1]) != self.m_color):  # capture
                    l.append(Action(state.m_agentPos, Position(r - 1, c - 1)))

                if c < (state.m_boardSize - 1) and (state.m_board[r - 1][c + 1] != Utils.empty) and (
                        Utils.get_color_piece(state.m_board[r - 1][c + 1]) != self.m_color):  # capture
                    l.append(Action(state.m_agentPos, Position(r - 1, c + 1)))

        return l
