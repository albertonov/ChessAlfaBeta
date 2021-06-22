import Utils
from Piece import Piece


class Knight(Piece):

    def __init__(self, color):
        self.m_color = color

        if color == 0:
            self.m_type = Utils.wKnight
        else:
            self.m_type = Utils.bKnight

    def get_possible_actions(self, state):

        return self.knight_moves(state)
