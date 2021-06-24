# This class contains the information needed to represent a state
# and some useful methods

import sys
import copy
import Utils
from Action import Action
from Position import Position


class State:
    m_board = None
    m_boardSize = -1
    isFinal = False
    profundidad = 3 #3 por defecto
    listaBlancas = []
    listaNegras =  []
    m_agentPos = -1
    turn = -1
    move = None


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
        self.listaBlancas = []
        self.listaNegras = []
        self.profundidad = prof



    def copy(self, memodict={}):
        newState = State(self.m_board, self.turn)
        newState.__dict__.update(self.__dict__)
        newState.m_boardSize = copy.deepcopy(self.m_boardSize, memodict)
        newState.listaBlancas = copy.deepcopy(self.listaBlancas, memodict)
        newState.m_board = copy.deepcopy(self.m_board, memodict)
        newState.m_agentPos = copy.deepcopy(self.m_agentPos, memodict)
        newState.listaNegras = copy.deepcopy(self.listaNegras, memodict)
        newState.turn = copy.deepcopy(self.turn, memodict)
        newState.move = copy.deepcopy(self.move, memodict)
        newState.profundidad = copy.deepcopy(self.profundidad, memodict)
        newState.isFinal = copy.deepcopy(self.isFinal, memodict)
        return newState

    # apply a given action over the current state -which remains unmodified. Return a new state

    def applyAction(self, action):

        newState = copy.deepcopy(self)
        newState.profundidad = newState.profundidad - 1
        piezaCapturada = self.m_board[action.m_finalPos.row][action.m_finalPos.col]
        pieza = self.m_board[action.m_initPos.row][action.m_initPos.col]
        if (piezaCapturada == Utils.wKing) or (piezaCapturada == Utils.bKing) :
            newState.isFinal = True


        #actualizacion de las listas
        if pieza <= 5 and pieza >= 0:
            #eliminamos la posicion antigua de la lista y anadimos la nueva
            newState.listaBlancas.remove((action.m_initPos.row, action.m_initPos.col))
            newState.listaBlancas.append((action.m_finalPos.row, action.m_finalPos.col))
            if piezaCapturada != Utils.empty:
                #si capturamos una pieza, la eliminamos de la lista rival
                newState.listaNegras.remove((action.m_finalPos.row, action.m_finalPos.col))

        else:
            #eliminamos la posicion antigua de la lista y anadimos la nueva
            newState.listaNegras.remove((action.m_initPos.row, action.m_initPos.col))
            newState.listaNegras.append((action.m_finalPos.row, action.m_finalPos.col))
            if piezaCapturada != Utils.empty:
                #si capturamos una pieza, la eliminamos de la lista rival
                newState.listaBlancas.remove((action.m_finalPos.row, action.m_finalPos.col))
    



        #Realizamos el movimiento

        if (pieza == Utils.wPawn and action.m_finalPos.row == 7):
            # Coronacion de peon blanco
            newState.m_board[action.m_finalPos.row][action.m_finalPos.col] = Utils.wQueen
        elif (pieza == Utils.bPawn and action.m_finalPos.row == 0):
            # Coronacion de peon negro
            newState.m_board[action.m_finalPos.row][action.m_finalPos.col] = Utils.bQueen
        else:
            #anadimos la pieza a la posicion final
            newState.m_board[action.m_finalPos.row][action.m_finalPos.col] = pieza

        #eliminamos la pieza de la posicion original
        newState.m_board[action.m_initPos.row][action.m_initPos.col] = Utils.empty

        newInitPos = Position(action.m_initPos.row, action.m_initPos.col)
        newFinalPos = Position(action.m_finalPos.row, action.m_finalPos.col)
        newState.move = Action(newInitPos,newFinalPos)

        return newState

    def crearListas(self):
        tam = len(self.m_board)
        for col in range(tam):
            for row in range(tam):
                if self.m_board[col][row] <= 5:
                    self.listaBlancas.append((col, row))

                elif self.m_board[col][row] >= 6 and self.m_board[col][row] <=11 :
                    self.listaNegras.append((col, row))


    def Utilidad(self):

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



        utilidad = 0
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
        for posX, posY in self.listaBlancas:
            numberPiece = self.m_board[posX][posY]
            utilidad += valuePieces[numberPiece]
            if numberPiece == Utils.wKnight:
                utilidad += wKnightEval[posX][posY]
            elif numberPiece == Utils.wQueen:
                utilidad += wQueenEval[posX][posY]
            elif numberPiece == Utils.wRook:
                utilidad += wRookEval[posX][posY]
            elif numberPiece == Utils.wPawn:
                utilidad += wPawnEval[posX][posY]
            elif numberPiece == Utils.wBishop:
                utilidad += wKnightEval[posX][posY]



        for posX, posY in self.listaNegras:
            numberPiece = self.m_board[posX][posY]
            utilidad += valuePieces[numberPiece]
            if numberPiece == Utils.bKnight:
                utilidad += bKnightEval[posX][posY]
            elif numberPiece == Utils.bQueen:
                utilidad += bQueenEval[posX][posY]
            elif numberPiece == Utils.bRook:
                utilidad += bRookEval[posX][posY]
            elif numberPiece == Utils.bPawn:
                utilidad += bPawnEval[posX][posY]
            elif numberPiece == Utils.bBishop:
                utilidad += bKnightEval[posX][posY]

        return utilidad

