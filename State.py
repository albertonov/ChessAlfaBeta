# This class contains the information needed to represent a state
# and some useful methods

import sys
import copy
import Utils
from Action import Action
import collections as q

from Position import Position


class State:
    m_board = None
    m_boardSize = -1
    isFinal = False
    depth = 4
    wElemList = []
    bElemList =  []
    m_agentPos = -1
    turn = -1
    move = None

    # constructor
    def __init__(self, board, turn):
        self.m_board = board
        self.turn = turn
        if (self.m_agentPos > 11):
            print("\n*** Invalid piece ***\n")
            sys.exit(0)
        else:
            if (self.m_agentPos > 5):
                self.m_color = 1  # black
        self.m_boardSize = len(board[0])
        self.wElemList = []
        self.bElemList = []
        self.reloadPositions() # carga posiciones iniciales


    # hard copy of an State
    def copy(self, memodict={}):
        # print '__deepcopy__(%s)' % str(memo)
        newState = State(self.m_board, self.turn)
        newState.__dict__.update(self.__dict__)
        newState.m_board = copy.deepcopy(self.m_board, memodict)
        newState.m_agentPos = copy.deepcopy(self.m_agentPos, memodict)
        #newState.m_color = copy.deepcopy(self.m_color, memodict)
        newState.m_boardSize = copy.deepcopy(self.m_boardSize, memodict)
        newState.wElemList = copy.deepcopy(self.wElemList, memodict)
        newState.bElemList = copy.deepcopy(self.bElemList, memodict)
        newState.turn = copy.deepcopy(self.turn, memodict)
        newState.move = copy.deepcopy(self.move, memodict)
        newState.depth = copy.deepcopy(self.depth, memodict)
        newState.isFinal = copy.deepcopy(self.isFinal, memodict)
        return newState

    # apply a given action over the current state -which remains unmodified. Return a new state

    def applyAction(self, action):
        turn = -1
        eaten = False
        newState = self.copy()
        pieceTaken = self.m_board[action.m_finalPos.row][action.m_finalPos.col]
        myPiece = self.m_board[action.m_initPos.row][action.m_initPos.col]
        if (pieceTaken == Utils.wKing) or (pieceTaken == Utils.bKing):
            self.isFinal = True
        if pieceTaken != Utils.empty:
            eaten = True
        if myPiece in range (0,6):
            turn = 0 # Blancas
        else:
            turn = 1 # Negras

        newState.m_board[action.m_initPos.row][action.m_initPos.col] = Utils.empty
        newState.m_board[action.m_finalPos.row][action.m_finalPos.col] = pieceTaken
        newState.depth = newState.depth - 1
        newInitPos = Position(action.m_initPos.row, action.m_initPos.col)
        newFinalPos = Position(action.m_finalPos.row, action.m_finalPos.col)
        newState.move = Action(newInitPos,newFinalPos)
        newState.updateList(turn, eaten, action)
        return newState

    def reloadPositions(self):
        for eachX in range(len(self.m_board)):
            for eachY in range(len(self.m_board)):
                if self.m_board[eachX][eachY] in range(0,6):#Blancas
                    self.wElemList.append((eachX,eachY))#por la derecha, tupla
                elif self.m_board[eachX][eachY] in range(6,12):#Negras
                    self.bElemList.append((eachX, eachY))#por la izqda, tupla


    def updateList(self, turn, eaten, action):
        if turn:#negras
            self.bElemList.remove((action.m_initPos.row,action.m_initPos.col))
            self.bElemList.append((action.m_finalPos.row,action.m_finalPos.col))
            if eaten:
                self.wElemList.remove((action.m_finalPos.row,action.m_finalPos.col))
        elif not turn:#blancas
            ElemToRemove = (action.m_initPos.row,action.m_initPos.col)
            self.wElemList.remove((action.m_initPos.row,action.m_initPos.col))
            self.wElemList.append((action.m_finalPos.row,action.m_finalPos.col))
            if eaten:
                self.bElemList.remove((action.m_finalPos.row,action.m_finalPos.col))

    def getEval(self):

        eval = 0
        valuePieces = {
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
            numberPiece = self.m_board[posX][posY]
            eval += valuePieces[numberPiece]
        for posX, posY in self.bElemList:
            numberPiece = self.m_board[posX][posY]
            eval += valuePieces[numberPiece]
        return eval

    def __hash__(self):
        unique_total = 0
        for each in self.m_board:
            unique_total += sum(each)
        return hash((self.m_agentPos.row, self.m_agentPos.col, self.m_agentPos, unique_total))
