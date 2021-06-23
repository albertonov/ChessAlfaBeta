# This class contains the information needed to represent a state
# and some useful methods

import sys
import copy
import Utils
from Action import Action
import collections as q

from Position import Position


class State:
    id = 0
    m_board = None
    m_boardSize = -1
    isFinal = False
    depth = 3
    wElemList = []
    bElemList =  []
    m_agentPos = -1
    turn = -1
    move = None
    valorFinal = 0
    father = None

    # constructor
    def __init__(self, board, turn, prof):
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
        self.depth = prof
        #self.crearListas() # carga posiciones iniciales



    # hard copy of an State
    def copy(self, memodict={}):
        newState = State(self.m_board, self.turn)
        newState.__dict__.update(self.__dict__)
        newState.m_boardSize = copy.deepcopy(self.m_boardSize, memodict)
        newState.wElemList = copy.deepcopy(self.wElemList, memodict)
        newState.m_board = copy.deepcopy(self.m_board, memodict)
        newState.m_agentPos = copy.deepcopy(self.m_agentPos, memodict)
        newState.bElemList = copy.deepcopy(self.bElemList, memodict)
        newState.turn = copy.deepcopy(self.turn, memodict)
        newState.move = copy.deepcopy(self.move, memodict)
        newState.depth = copy.deepcopy(self.depth, memodict)
        newState.isFinal = copy.deepcopy(self.isFinal, memodict)
        return newState

    # apply a given action over the current state -which remains unmodified. Return a new state

    def applyAction(self, action):
        turn = -1
        captura = False
        newState = copy.deepcopy(self)
        newState.id = self.id + 1
        piezaCapturada = self.m_board[action.m_finalPos.row][action.m_finalPos.col]
        pieza = self.m_board[action.m_initPos.row][action.m_initPos.col]
        if (piezaCapturada == Utils.wKing) or (piezaCapturada == Utils.bKing) :
            newState.isFinal = True
        if piezaCapturada != Utils.empty:
            captura = True


        if pieza <= 5 and pieza >= 0:
            newState.wElemList.remove((action.m_initPos.row, action.m_initPos.col))
            newState.wElemList.append((action.m_finalPos.row, action.m_finalPos.col))
            if captura:
                newState.bElemList.remove((action.m_finalPos.row, action.m_finalPos.col))

        else:
            newState.bElemList.remove((action.m_initPos.row, action.m_initPos.col))
            newState.bElemList.append((action.m_finalPos.row, action.m_finalPos.col))
            if captura:
                newState.wElemList.remove((action.m_finalPos.row, action.m_finalPos.col))
    


        newState.m_board[action.m_initPos.row][action.m_initPos.col] = Utils.empty

        if (pieza == Utils.wPawn and action.m_finalPos.row == 7):
            newState.m_board[action.m_finalPos.row][action.m_finalPos.col] = Utils.wQueen
        elif (pieza == Utils.bPawn and action.m_finalPos.row == 0):
            newState.m_board[action.m_finalPos.row][action.m_finalPos.col] = Utils.bQueen
        else:
            newState.m_board[action.m_finalPos.row][action.m_finalPos.col] = pieza


        newState.depth = newState.depth - 1
        newInitPos = Position(action.m_initPos.row, action.m_initPos.col)
        newFinalPos = Position(action.m_finalPos.row, action.m_finalPos.col)
        newState.move = Action(newInitPos,newFinalPos)

        return newState

    def crearListas(self):
        self.wElemList.clear()
        self.bElemList.clear()
        for eachX in range(len(self.m_board)):
            for eachY in range(len(self.m_board)):
                if self.m_board[eachX][eachY] in range(0,6):#Blancas
                    self.wElemList.append((eachX,eachY))#por la derecha, tupla
                elif self.m_board[eachX][eachY] in range(6,12):#Negras
                    self.bElemList.append((eachX, eachY))#por la izqda, tupla


    def getEval(self):

        bKnightEval =[  [50, 40, 30, 30, 30, 30, 40, 50],
                        [40, 20,  0,  0,  0,  0, 20, 40],
                        [30,  0,-10,-15,-15,-10,  0, 30],
                        [30, -5,-15,-20,-20,-15, -5, 30],
                        [30,  0,-15,-20,-20,-15,  0, 30],
                        [30, -5,-10,-15,-15,-10, -5, 30],
                        [40, 20,  0, -5, -5,  0, 20, 40],
                        [50, 40, 30, 30, 30, 30, 40, 50]]

        wKnightEval = [[-50,-40,-30,-30,-30,-30,-40,-50],
                       [-40, -20, 0, 0, 0, 0, -20, -40],
                       [-30, 5, 10, 15, 15, 10, 5, -30],
                       [-30, 0, 15, 20, 20, 15, 0, -30],
                       [-30, 5, 15, 20, 20, 15, 5, -30],
                       [-30, 0, 10, 15, 15, 10, 0, -30],
                       [-40, -20, 0, 5, 5, 0, -20, -40],
                       [-50,-40,-30,-30,-30,-30,-40,-50]]

        bQueenEval = [
            [20, 10, 10,  5,  5, 10, 10, 20],
            [10,  0,  0,  0,  0,  0,  0, 10],
            [10,  0, -5, -5, -5, -5,  0, 10],
            [5,   0, -5, -5, -5, -5,  0,  5],
            [0,   0, -5, -5, -5, -5,  0,  5],
            [10,  0, -5, -5, -5, -5,  0, 10],
            [10,  0, -5,  0,  0,  0,  0, 10],
            [20, 10, 10,  5,  5, 10, 10, 20]
        ]


        wQueenEval = [
            [-20,-10,-10, -5, -5,-10,-10,  -20],
            [-10, 0,  0,  0,  0,  0,   0,  -10],
            [-10, 0,  5,  5,  5,  5,   0,  -10],
            [-10, 0,  5,  5,  5,  5,   0,  -10],
            [-10, 0,  5,  5,  5,  5,   0,  -10],
            [-10, 0,  5,  5,  5,  5,   0,  -10],
            [-10, 0,  0,  0,  0,  0,   0,  -10],
            [-20,-10,-10,-5, -5, -10, -10, -20]
        ]

        wRookEval = [
            [0,  0,  0,  0,  0,  0,  0,  0],
            [-5,  0,  0,  0,  0,  0,  0,  -5],
            [-5,  0,  0,  0,  0,  0,  0,  -5],
            [-5,  0,  0,  0,  0,  0,  0,  -5],
            [-5,  0,  0,  0,  0,  0,  0,  -5],
            [-5,  0,  0,  0,  0,  0,  0,  -5],
            [-5,  0,  0,  0,  0,  0,  0,  -5],
            [0,  0,  0,  0,  0,  0,  0,  0]]

        bRookEval = [
            [0,  0,  0,  0,  0,  0,  0,  0],
            [5,  0,  0,  0,  0,  0,  0,  5],
            [5,  0,  0,  0,  0,  0,  0,  5],
            [5,  0,  0,  0,  0,  0,  0,  5],
            [5,  0,  0,  0,  0,  0,  0,  5],
            [5,  0,  0,  0,  0,  0,  0,  5],
            [5,  0,  0,  0,  0,  0,  0,  5],
            [0,  0,  0,  0,  0,  0,  0,  0]
        ]

        bPawnEval = [
            [0,     0,    0,   0,    0,    0,   0,   0],
            [-50, -50,  -50, -50,  -50,  -50, -50, -50],
            [-10, -10,  -20, -30,  -30,  -20, -10, -10],
            [-5,   -5,  -10, -25,  -25,  -10,  -5,  -5],
            [0,     0,    0, -20,  -20,    0,   0,   0],
            [-5,    5,   10,   0,    0,   10,   5,  -5],
            [-5,  -10,  -10,  20,   20,  -10, -10,  -5],
            [0,     0,    0,   0,    0,    0,   0,   0]
        ]


        wPawnEval = [
            [0,   0,   0,  0,   0,   0,  0,  0],
            [5,  10,  10,-20, -20,  10, 10,  5],
            [5,  -5, -10,  0,   0, -10, -5,  5],
            [0,   0,   0, 20,  20,   0,  0,  0],
            [5,   5,  10, 25,  25,  10,  5,  5],
            [10, 10,  20, 30,  30,  20, 10, 10],
            [50, 50,  50, 50,  50,  50, 50, 50],
            [0,   0,   0,  0,   0,   0,  0,  0]
        ]



        eval = 0
        valuePieces = {
            0: +100,
            1: +500,
            2: +330,
            3: +320,
            4: +900,
            5: +20000,
            6: -100,
            7: -500,
            8: -330,
            9: -320,
            10: -900,
            11: -20000
        }
        for posX, posY in self.wElemList:
            numberPiece = self.m_board[posX][posY]
            eval += valuePieces[numberPiece]
            if numberPiece == Utils.wKnight:
                eval += wKnightEval[posX][posY]
            elif numberPiece == Utils.wQueen:
                eval += wQueenEval[posX][posY]
            elif numberPiece == Utils.wRook:
                eval += wRookEval[posX][posY]
            elif numberPiece == Utils.wPawn:
                eval += wPawnEval[posX][posY]




        for posX, posY in self.bElemList:
            numberPiece = self.m_board[posX][posY]
            eval += valuePieces[numberPiece]
            if numberPiece == Utils.bKnight:
                eval += bKnightEval[posX][posY]
            elif numberPiece == Utils.bQueen:
                eval += bQueenEval[posX][posY]
            elif numberPiece == Utils.bRook:
                eval += bRookEval[posX][posY]
            elif numberPiece == Utils.bPawn:
                eval += bPawnEval[posX][posY]
        return eval

