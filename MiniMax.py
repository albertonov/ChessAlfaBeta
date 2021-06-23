import copy
import Utils
from Position import Position
from Statistics import Statistics

MINUS_INF = -1000000
PLUS_INF = 1000000

stats = Statistics()


def successors(state, turn):
    stats.expanded = stats.expanded + 1
    new_states = []
    if turn:  # Whites
        for pos in state.wElemList:
            states = get_states(pos[0], pos[1], state)
            stats.generated = stats.generated + len(states)
            new_states.extend(states)
    else:  # Blacks
        for pos in state.bElemList:
            states = get_states(pos[0], pos[1], state)
            stats.generated = stats.generated + len(states)
            new_states.extend(states)
    return new_states


def get_states(x, y, state):
    state_list = []
    value = state.m_board[x][y]
    piece = Utils.piece_factory(value)
    # make sure it is a different state
    mod_state = copy.deepcopy(state)
    mod_state.m_agentPos = Position(x, y)
    actions = piece.get_possible_actions(mod_state)
    for each in actions:
        state_list.append(mod_state.applyAction(each))
    return state_list


def minimax(state, turn, pruning):
    stats.init_eval = state.getEval()
    if turn:
        v, m = minvalue(state, turn, None, pruning=pruning)
        stats.final_eval = v
        return v, m, stats
    else:
        v, m = maxvalue(state, turn, None, pruning=pruning)
        stats.final_eval = v
        return v, m, stats


def minvalue(state, turn, m, alfa=MINUS_INF, beta=PLUS_INF, pruning=False):
    turn = (turn + 1) % 2
    if state.isFinal or state.depth == 0:
        m = state.move
        return state.getEval(), m
    v = PLUS_INF
    for st in successors(state, turn):
        # min(v, minimax minimax)
        act_v = maxvalue(st, turn, m, alfa, beta, pruning)[0]
        if act_v < v:
            v = act_v
            m = st.move
        if pruning:
            if v <= alfa:
                return v, m
            beta = min(v, beta)
    return v, m


def maxvalue(state, turn, m, alfa=MINUS_INF, beta=PLUS_INF, pruning=False):
    turn = (turn + 1) % 2
    if state.isFinal or state.depth == 0:
        m = state.move
        return state.getEval(), m
    v = MINUS_INF
    for st in successors(state, turn):
        # max(v, minimax minimax)
        act_v = minvalue(st, turn, m, alfa, beta, pruning)[0]
        if act_v > v:
            v = act_v
            m = st.move
        if pruning:
            if v >= beta:
                return v, m
            alfa = max(v, alfa)
    return v, m
