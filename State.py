import sys
import copy
import Utils
from Action import Action
from Position import Position


class State:
    id = 0
    m_board = None
    m_boardSize = -1
    isFinal = False
    depth = 3
    wElemList = []
    bElemList = []
    m_agentPos = -1
    turn = -1
    move = None

    # constructor
    def __init__(self, board, turn):
        self.m_board = board
        self.turn = turn
        if self.m_agentPos > 11:
            print("\n*** Invalid piece ***\n")
            sys.exit(0)
        else:
            if self.m_agentPos > 5:
                self.m_color = 1  # black
        self.m_boardSize = len(board[0])
        self.wElemList = []
        self.bElemList = []

    # apply a given action over the current state -which remains unmodified. Return a new state

    def apply_action(self, action):
        turn = -1
        eaten = False
        new_state = copy.deepcopy(self)
        new_state.id = self.id + 1
        piece_taken = self.m_board[action.m_finalPos.row][action.m_finalPos.col]
        my_piece = self.m_board[action.m_initPos.row][action.m_initPos.col]
        if (piece_taken == Utils.wKing) or (piece_taken == Utils.bKing):
            new_state.isFinal = True
        if piece_taken != Utils.empty:
            eaten = True
        if my_piece in range(0, 6):
            turn = 0  # Whites
        else:
            turn = 1  # Blacks

        new_state.update_list(turn, eaten, action)

        new_state.m_board[action.m_initPos.row][action.m_initPos.col] = Utils.empty

        if my_piece == Utils.wPawn and action.m_finalPos.row == 7:
            new_state.m_board[action.m_finalPos.row][action.m_finalPos.col] = Utils.wQueen
        elif my_piece == Utils.bPawn and action.m_finalPos.row == 0:
            new_state.m_board[action.m_finalPos.row][action.m_finalPos.col] = Utils.bQueen
        else:
            new_state.m_board[action.m_finalPos.row][action.m_finalPos.col] = my_piece

        new_state.depth = new_state.depth - 1
        new_init_pos = Position(action.m_initPos.row, action.m_initPos.col)
        new_final_pos = Position(action.m_finalPos.row, action.m_finalPos.col)
        new_state.move = Action(new_init_pos, new_final_pos)

        return new_state

    def reload_positions(self, depth):
        self.wElemList.clear()
        self.bElemList.clear()
        self.depth = depth
        for eachX in range(len(self.m_board)):
            for eachY in range(len(self.m_board)):
                if self.m_board[eachX][eachY] in range(0, 6):
                    self.wElemList.append((eachX, eachY))
                elif self.m_board[eachX][eachY] in range(6, 12):
                    self.bElemList.append((eachX, eachY))

    def update_list(self, turn, eaten, action):
        if turn:  # blacks
            self.bElemList.remove((action.m_initPos.row, action.m_initPos.col))
            self.bElemList.append((action.m_finalPos.row, action.m_finalPos.col))
            if eaten:
                self.wElemList.remove((action.m_finalPos.row, action.m_finalPos.col))
        elif not turn:  # whites
            self.wElemList.remove((action.m_initPos.row, action.m_initPos.col))
            self.wElemList.append((action.m_finalPos.row, action.m_finalPos.col))
            if eaten:
                self.bElemList.remove((action.m_finalPos.row, action.m_finalPos.col))

    def get_eval(self):
        eval = 0
        value_pieces = {
            0: +1,
            1: +5,
            2: +3,
            3: +3,
            4: +10,
            5: +500,
            6: -1,
            7: -5,
            8: -3,
            9: -3,
            10: -10,
            11: -500
        }
        for posX, posY in self.wElemList:
            number_piece = self.m_board[posX][posY]
            eval += value_pieces[number_piece]
        for posX, posY in self.bElemList:
            number_piece = self.m_board[posX][posY]
            eval += value_pieces[number_piece]

        return eval


