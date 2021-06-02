import copy


class Position:
    row = 0
    col = 0

    # constructor
    def __init__(self, r, c):
        self.row = r
        self.col = c

    # equals compares if the received position is equals to the member one
    def __eq__(self, other):
        # print("self:",self)
        # print("other:",other)
        if (self.row != other.row): return False
        if (self.col != other.col): return False
        return True

    def __str__(self):
        return "(" + str(self.row) + "," + str(self.col) + ")"

    # creates a hard copy of the object
    def copy(self, memodict={}):
        # print '__deepcopy__(%s)' % str(memo)
        new_p = Position(self.row, self.col)
        new_p.__dict__.update(self.__dict__)
        new_p.row = copy.deepcopy(self.row, memodict)
        new_p.col = copy.deepcopy(self.col, memodict)
        return new_p


if __name__ == '__main__':
    p1 = Position(1, 2)
    p2 = p1
    p3 = p1.copy()

    # p4 = copy.deepcopy(p1)
    print(id(p1))
    print(id(p2))
    print(id(p3))

    # print(id(p4))
    p1.row, p1.col = 0, 0
    print(p1.row, p1.col)
    print(p2.row, p2.col)
    print(p3.row, p3.col)

    # print(p4.row,p4.col)
