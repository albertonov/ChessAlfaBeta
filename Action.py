# in this class we define a basic action for our problem. Going from position p0 to position p1.

from Position import Position


class Action:
    m_initPos = None
    m_finalPos = None

    # constructor
    def __init__(self, p0, p1):
        self.m_initPos = p0;
        self.m_finalPos = p1;

    # the cost of a given action is: 1 + maximum of the horizontal/vertical traveled distance
    def getCost(self):
        return 1 + max(abs(self.m_initPos.row - self.m_finalPos.row), abs(self.m_initPos.col - self.m_finalPos.col))

    # to String method, just for printing the solution
    def __str__(self):
        return "[ (" + str(self.m_initPos.row) + "," + str(self.m_initPos.col) + ") -> (" + str(
            self.m_finalPos.row) + "," + str(self.m_finalPos.col) + ") ]";

