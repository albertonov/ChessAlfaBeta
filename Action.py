class Action:
    m_initPos = None
    m_finalPos = None

    # constructor
    def __init__(self, p0, p1):
        self.m_initPos = p0
        self.m_finalPos = p1

    # to String method, just for printing the solution
    def __str__(self):
        return "[ (" + str(self.m_initPos.row) + "," + str(self.m_initPos.col) + ") -> (" + str(
            self.m_finalPos.row) + "," + str(self.m_finalPos.col) + ") ]";
