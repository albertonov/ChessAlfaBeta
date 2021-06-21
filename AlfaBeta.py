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

MINUS_INF = -1000000
PLUS_INF = 1000000
expanded = 0
generated = 0


def incrementExpanded(increment):
    global expanded
    expanded = expanded + increment


def incrementGenerated(increment):
    global generated
    generated = generated + increment


def successors(state, turn):
    incrementExpanded(1)
    newstates = []
    if (turn):  # Whites
        for pos in state.wElemList:
            states = get_states(pos[0], pos[1], state)
            incrementGenerated(len(states))
            newstates.extend(states)
    else:  # Blacks
        for pos in state.bElemList:
            states = get_states(pos[0], pos[1], state)
            incrementGenerated(len(states))
            newstates.extend(states)
    return newstates


def get_states(x, y, state):
    state_list = []
    value = state.m_board[x][y]
    piece = piece_factory(value)
    # make sure it is a different state
    mod_state = copy.deepcopy(state)
    mod_state.m_agentPos = Position(x, y)
    actions = piece.getPossibleActions(mod_state)
    for each in actions:
        state_list.append(mod_state.applyAction(each))
    return state_list


def piece_factory(value):
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
        return Bishop(0)
    elif value == Utils.bBishop:
        return Bishop(1)
    elif value == Utils.wKnight:
        return Knight(0)
    elif value == Utils.bKnight:
        return Knight(1)
    else:
        return None


def alfa_beta(state, turn):
    if turn:
        v, m = minvalue(state, turn, None, MINUS_INF, PLUS_INF)
        return v, m, generated, expanded
    else:
        v, m = maxvalue(state, turn, None, MINUS_INF, PLUS_INF)
        return v, m, generated, expanded


def minvalue(state, turn, m, alfa, beta):
    turn = (turn + 1) % 2
    if state.isFinal or state.depth == 0:
        m = state.move
        return state.getEval(), m
    v = PLUS_INF
    for st in successors(state, turn):
        # min(v, minimax alfa_beta)
        act_v = maxvalue(st, turn, m, alfa, beta)[0]
        if act_v < v:
            v = act_v
            m = st.move
        if v <= alfa:
            return v, m
        beta = min(v, beta)
    return v, m


def maxvalue(state, turn, m, alfa, beta):
    turn = (turn + 1) % 2
    if state.isFinal or state.depth == 0:
        m = state.move
        return state.getEval(), m
    v = MINUS_INF
    for st in successors(state, turn):
        # max(v, minimax alfa_beta)
        act_v = minvalue(st, turn, m, alfa, beta)[0]
        if act_v > v:
            v = act_v
            m = st.move
        if v >= beta:
            return v, m
        alfa = max(v, alfa)
    return v, m
