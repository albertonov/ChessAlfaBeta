# import java.util.ArrayList;

# this class implements the getPossibleActions for each type of piece

import Utils
from Position import Position
from Action import Action
from State import State


class Piece:
    # this method must be completed with all the possible pieces

    def __init__(self):
        m_color = -1
        m_type = -1

        self.coordinates = []  # coordinates for Knight and King getMoves method. Setted on Kinght and King constructor, none by other pieces

    def getPossibleActions(self, state):

        return None  # never arrive here

    # horizontal left moves
    def getHorizontalLeftMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

        busyCell = False
        for c in range(col0 - 1, -1, -1):
            if not busyCell:
                if state.m_board[row0][c] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(row0, c))
                    l.append(action)
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[row0][c]):  # capture piece
                        action = Action(state.m_agentPos, Position(row0, c))
                        l.append(action)

        return l

    # horizontal right moves
    def getHorizontalRightMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

        busyCell = False
        for c in range(col0 + 1, state.m_boardSize):
            if not busyCell:
                if state.m_board[row0][c] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(row0, c))
                    l.append(action)
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[row0][c]):  # capture piece
                        action = Action(state.m_agentPos, Position(row0, c))
                        l.append(action)

        return l

    # vertical up moves
    def getVerticalUpMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

        busyCell = False
        for r in range(row0 - 1, -1, -1):
            if not busyCell:
                if state.m_board[r][col0] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(r, col0))
                    l.append(action)
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[r][col0]):  # capture piece
                        action = Action(state.m_agentPos, Position(r, col0))
                        l.append(action)
        return l

    # vertical down moves
    def getVerticalDownMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

        busyCell = False
        for r in range(row0 + 1, state.m_boardSize):
            if not busyCell:
                if state.m_board[r][col0] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(r, col0))
                    l.append(action)
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[r][col0]):  # capture piece
                        action = Action(state.m_agentPos, Position(r, col0))
                        l.append(action)

        return l

    def getDiagonalDownRightMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col;
        r = row0 + 1  # r tiende a aumentar
        c = col0 + 1  # c tiende a aumentar
        busyCell = False

        while (r < state.m_boardSize and c < state.m_boardSize):
            if not busyCell:
                if state.m_board[r][c] == Utils.empty:  # add action
                    l.append(Action(state.m_agentPos, Position(r, c)))
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[r][c]):
                        l.append(Action(state.m_agentPos, Position(r, c)))
            r = r + 1
            c = c + 1

        return l

    def getDiagonalDownLeftMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col;
        r = row0 + 1  # r tiende a aumentar
        c = col0 - 1  # c tiende a disminuir
        busyCell = False

        while (r < state.m_boardSize and c >= 0):
            if not busyCell:
                if state.m_board[r][c] == Utils.empty:  # add action
                    l.append(Action(state.m_agentPos, Position(r, c)))
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[r][c]):
                        l.append(Action(state.m_agentPos, Position(r, c)))
            r = r + 1
            c = c - 1

        return l

    def getDiagonalUpLeftMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col;
        r = row0 - 1  # r tiende a disminuir
        c = col0 - 1  # c tiende a disminuir
        busyCell = False

        while (r >= 0 and c >= 0):
            if not busyCell:
                if state.m_board[r][c] == Utils.empty:  # add action
                    l.append(Action(state.m_agentPos, Position(r, c)))
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[r][c]):
                        l.append(Action(state.m_agentPos, Position(r, c)))
            r = r - 1
            c = c - 1
        return l

    def getDiagonalUpRightMoves(self, state):
        l = []
        agentColor = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col;
        r = row0 - 1  # r tiende a disminuir
        c = col0 + 1  # c tiende a aumentar
        busyCell = False

        while (r >= 0 and c < state.m_boardSize):
            if not busyCell:
                if state.m_board[r][c] == Utils.empty:  # add action
                    l.append(Action(state.m_agentPos, Position(r, c)))
                else:
                    busyCell = True
                    if agentColor != Utils.getColorPiece(state.m_board[r][c]):
                        l.append(Action(state.m_agentPos, Position(r, c)))
            r = r - 1
            c = c + 1
        return l

    def getMovesByCoordinates(self, state):
        # only for knight and king. Needs a default list of tuples of coordinates setted in King and Knight constructor respectively
        r = state.m_agentPos.row
        c = state.m_agentPos.col

        oponent_color = -1
        if self.m_color == 0:  # white king
            oponent_color = 1
        elif self.m_color == 1:  # black king
            oponent_color = 0

        l = []
        for x, y in self.coordinates:
            r1 = r + x
            c1 = c + y
            if r1 >= 0 and r1 < state.m_boardSize and c1 >= 0 and c1 < state.m_boardSize:  # comprobomas si esta fuera del tablero

                if state.m_board[r1][c1] == Utils.empty:
                    l.append(Action(state.m_agentPos, Position(r1, c1)))
                elif Utils.getColorPiece(state.m_board[r1][c1]) == oponent_color:
                    l.append(Action(state.m_agentPos, Position(r1, c1)))

        return l
