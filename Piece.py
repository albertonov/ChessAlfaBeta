import Utils
from Position import Position
from Action import Action


class Piece:

    def __init__(self):
        m_color = -1
        m_type = -1

    def get_possible_actions(self, state):

        return None  # never arrive here

    # horizontal left moves
    def get_horizontal_left_moves(self, state):
        l = []
        agent_color = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col

        busy_cell = False
        for c in range(col0 - 1, -1, -1):
            if not busy_cell:
                if state.m_board[row0][c] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(row0, c))
                    l.append(action)
                else:
                    busy_cell = True
                    if agent_color != Utils.get_color_piece(state.m_board[row0][c]):  # capture piece
                        action = Action(state.m_agentPos, Position(row0, c))
                        l.append(action)

        return l

    # horizontal right moves
    def get_horizontal_right_moves(self, state):
        l = []
        agent_color = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col

        busy_cell = False
        for c in range(col0 + 1, state.m_boardSize):
            if not busy_cell:
                if state.m_board[row0][c] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(row0, c))
                    l.append(action)
                else:
                    busy_cell = True
                    if agent_color != Utils.get_color_piece(state.m_board[row0][c]):  # capture piece
                        action = Action(state.m_agentPos, Position(row0, c))
                        l.append(action)

        return l

    # vertical up moves
    def get_vertical_up_moves(self, state):
        l = []
        agent_color = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

        busy_cell = False
        for r in range(row0 - 1, -1, -1):
            if not busy_cell:
                if state.m_board[r][col0] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(r, col0))
                    l.append(action)
                else:
                    busy_cell = True
                    if agent_color != Utils.get_color_piece(state.m_board[r][col0]):  # capture piece
                        action = Action(state.m_agentPos, Position(r, col0))
                        l.append(action)
        return l

    # vertical down moves
    def get_vertical_down_moves(self, state):
        l = []
        agent_color = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col;

        busy_cell = False
        for r in range(row0 + 1, state.m_boardSize):
            if not busy_cell:
                if state.m_board[r][col0] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(r, col0))
                    l.append(action)
                else:
                    busy_cell = True
                    if agent_color != Utils.get_color_piece(state.m_board[r][col0]):  # capture piece
                        action = Action(state.m_agentPos, Position(r, col0))
                        l.append(action)

        return l

    def get_diagonal_down_right_moves(self, state):
        l = []
        agent_color = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col
        r = row0 + 1
        c = col0 + 1
        busy_cell = False

        while r < state.m_boardSize and c < state.m_boardSize:
            if not busy_cell:
                if state.m_board[r][c] == Utils.empty:  # add action
                    l.append(Action(state.m_agentPos, Position(r, c)))
                else:
                    busy_cell = True
                    if agent_color != Utils.get_color_piece(state.m_board[r][c]):  # capture piece
                        l.append(Action(state.m_agentPos, Position(r, c)))
            r = r + 1
            c = c + 1

        return l

    def get_diagonal_down_left_moves(self, state):
        l = []
        agent_color = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col
        r = row0 + 1
        c = col0 - 1
        busy_cell = False

        while r < state.m_boardSize and c >= 0:
            if not busy_cell:
                if state.m_board[r][c] == Utils.empty:  # add action
                    l.append(Action(state.m_agentPos, Position(r, c)))
                else:
                    busy_cell = True
                    if agent_color != Utils.get_color_piece(state.m_board[r][c]):  # capture piece
                        l.append(Action(state.m_agentPos, Position(r, c)))
            r = r + 1
            c = c - 1

        return l

    def get_diagonal_up_left_moves(self, state):
        l = []
        agent_color = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col
        r = row0 - 1
        c = col0 - 1
        busy_cell = False

        while r >= 0 and c >= 0:
            if not busy_cell:
                if state.m_board[r][c] == Utils.empty:  # add action
                    l.append(Action(state.m_agentPos, Position(r, c)))
                else:
                    busy_cell = True
                    if agent_color != Utils.get_color_piece(state.m_board[r][c]):  # capture piece
                        l.append(Action(state.m_agentPos, Position(r, c)))
            r = r - 1
            c = c - 1
        return l

    def get_diagonal_up_right_moves(self, state):
        l = []
        agent_color = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col
        r = row0 - 1
        c = col0 + 1
        busy_cell = False

        while r >= 0 and c < state.m_boardSize:
            if not busy_cell:
                if state.m_board[r][c] == Utils.empty:  # add action
                    l.append(Action(state.m_agentPos, Position(r, c)))
                else:
                    busy_cell = True
                    if agent_color != Utils.get_color_piece(state.m_board[r][c]):  # capture piece
                        l.append(Action(state.m_agentPos, Position(r, c)))
            r = r - 1
            c = c + 1
        return l

    def get_immediate_moves(self, state):
        l = []
        agent_color = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col
        final_element = state.m_boardSize
        for r in range(row0 - 1, row0 + 2):
            for c in range(col0 - 1, col0 + 2):
                if r in range(0, final_element) and c in range(0, final_element):
                    if state.m_board[r][c] == Utils.empty:  # add action
                        action = Action(state.m_agentPos, Position(r, c))
                        l.append(action)
                    elif agent_color != Utils.get_color_piece(state.m_board[r][c]):  # capture piece
                        action = Action(state.m_agentPos, Position(r, c))
                        l.append(action)

        return l

    def knight_moves(self, state):
        l = []
        agent_color = self.m_color
        row0, col0 = state.m_agentPos.row, state.m_agentPos.col
        final_element = state.m_boardSize
        r_range = [-2, -2, -1, -1, 1, 1, 2, 2]
        c_range = [1, -1, 2, -2, 2, -2, 1, -1]
        valid = range(0, final_element)
        x = zip(r_range, c_range)
        for r_gen, c_gen in x:
            r, c = row0 + r_gen, col0 + c_gen
            if r in valid and c in valid:
                if state.m_board[r][c] == Utils.empty:  # add action
                    action = Action(state.m_agentPos, Position(r, c))
                    l.append(action)
                else:
                    if agent_color != Utils.get_color_piece(state.m_board[r][c]):  # capture piece
                        action = Action(state.m_agentPos, Position(r, c))
                        l.append(action)
        return l
