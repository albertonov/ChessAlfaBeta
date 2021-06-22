import Utils
from Piece import Piece


class King(Piece):

    def __init__(self, color):
        self.m_color = color

        if color == 0:
            self.m_type = Utils.wKing
        else:
            self.m_type = Utils.bKing

    def get_possible_actions(self, state):
        listing = []
        listing += self.get_immediate_moves(state)

        return listing
