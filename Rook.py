import Utils
from Piece import Piece


class Rook(Piece):

    def __init__(self, color):
        self.m_color = color

        if color == 0:
            self.m_type = Utils.wRook
        else:
            self.m_type = Utils.bRook

    def get_possible_actions(self, state):
        l = []

        l += self.get_horizontal_left_moves(state)
        l += self.get_horizontal_right_moves(state)
        l += self.get_vertical_down_moves(state)
        l += self.get_vertical_up_moves(state)

        return l
