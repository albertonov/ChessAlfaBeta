import copy
import sys
import Utils
from State import State
import Piece
import math as m
from Piece import Piece
from Rook import Rook
from Knight import Knight
from Pawn import Pawn
from King import King
from Bishop import Bishop
from Queen import Queen
from Position import Position




def Sucesores(state, turn):
    newStates = []
    if(turn):                       #juegan blancas
        for pos in state.wElemList:
            newStates.extend(getStates(pos[0],pos[1],state))
    else:                           #juegan negras
        for pos in state.bElemList:
            newStates.extend(getStates(pos[0],pos[1],state))
    return newStates


def getStates(x,y,state):
    stateList = []
    value = state.m_board[x][y]
    pieza = piezaFactory(value)
    modState = copy.deepcopy(state)#hardcopy del estado, para modificar agente/color
    modState.m_agentPos = Position(x, y)
    actions = pieza.getPossibleActions(modState)
    for each in actions:
        stateList.append(modState.applyAction(each))
    return stateList



def piezaFactory(value):
        if value == Utils.wPawn:
            return Pawn(0)
        elif value == Utils.bPawn:
            return Pawn(1)
        elif value == Utils.wRook:
            return Rook(0)
        elif value == Utils.bRook:
            return Rook(1)
        elif value == Utils.wKing:
            return King(0)
        elif value == Utils.bKing:
            return King(1)
        elif value == Utils.wQueen:
            return Queen(0)
        elif value == Utils.bQueen:
            return Queen(1)
        elif value == Utils.wBishop:
            return  Bishop(0)
        elif value == Utils.bBishop:
            return Bishop(1)
        elif value == Utils.wKnight:
            return Knight(0)
        elif value == Utils.bKnight:
            return Knight(1)
        else:
            return None

def MiniMax (state, turn):
    return  MaxValue(state, turn)



def MinValue(state, turn):
    turn = (turn+1)%2
    if state.isFinal or state.depth == 0:
        return state.getEval()
    v = 1000000
    for st in Sucesores(state,turn):
        v = min(v, MaxValue(st, turn))
    return v
def MaxValue(state, turn):
    turn = (turn+1)%2
    if state.isFinal or state.depth == 0:
        return state.getEval()
    v = -10000000
    for st in Sucesores(state, turn):
        v = max(v, MinValue(st, turn))
    return v



# main to test the methods

if __name__ == '__main__':
    st = Utils.getChessInstancePosition( 0.4, 1771, 0)
    print(st.m_board)
    st.reloadPositions()
    Utils.printBoard(st)


    print(MiniMax(st, 0))
