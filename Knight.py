import Utils
from Position import Position
from Piece import Piece
from Action import Action


# this class implements the getPossibleActions for each type of piece

class Knight(Piece):

    # constructor
    def __init__(self, color):
        self.m_color = color
        self.coordinates = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
        if color == 0:
            self.m_type = Utils.wKnight
        else:
            self.m_type = Utils.bKnight

    # this method must be completed with all the possible pieces
    def getPossibleActions(self, state):

        return self.getMovesByCoordinates(state)