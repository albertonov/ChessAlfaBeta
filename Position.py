import copy


class Position:
    row = 0
    col = 0

    def __init__(self, r, c):
        self.row = r
        self.col = c

    def __eq__(self, other):
        if (self.row != other.row): return False
        if (self.col != other.col): return False
        return True

    def __str__(self):
        return "(" + str(self.row) + "," + str(self.col) + ")"


