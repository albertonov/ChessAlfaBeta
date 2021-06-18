import Utils
from Position import Position
from Piece import Piece
from Action import Action

# this class implements the getPossibleActions for each type of piece

class King(Piece):

    # constructor
    def __init__(self, color):
        self.m_color = color
        self.coordinates = [(-1, -1), (-1, 0), (-1, +1), (0, +1), (+1, +1), (+1, 0), (+1, -1), (0, -1)]

        if color == 0:
            self.m_type = Utils.wKing
        else:
            self.m_type = Utils.bKing

    # this method must be completed with all the possible pieces
    def getPossibleActions(self, state):

        return self.getMovesByCoordinates(state)


