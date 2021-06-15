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
    if turn:
        v, m = MinValue(state, turn, None)
        return v, m
    else:
        v, m = MaxValue(state, turn, None)
        return v, m



def MinValue(state, turn,m):
    turn = (turn+1)%2
    if state.isFinal or state.depth == 0:
        m = state.move
        return state.getEval(), m
    v = 1000000
    for st in Sucesores(state,turn):
        act_v = MaxValue(st, turn,m)[0]
        if act_v<v:
            v = act_v
            m = st.move
    return v,m
def MaxValue(state, turn,m):
    turn = (turn+1)%2
    if state.isFinal or state.depth == 0:
        m = state.move
        return state.getEval(), m
    v = -10000000
    for st in Sucesores(state, turn):
        act_v = MinValue(st, turn,m)[0]
        if act_v>v:
            v = act_v
            m = st.move
    return v,m



# main to test the methods

if __name__ == '__main__':
    st = Utils.getChessInstancePosition(0.2, 100, 0)
    print(st.m_board)
    st.reloadPositions()
    Utils.printBoard(st)


    v, m = (MiniMax(st, 0))
    print(f"Evaluation value is {v}")
    print(f"Action is ${m}")
