import Utils


nodosGeneradosMM = 0
nodosExpandidosMM = 0


def setToZeroExpandedAndGeneratedInMM():
    global nodosGeneradosMM
    nodosGeneradosMM = 0
    global nodosExpandidosMM
    nodosExpandidosMM = 0

def getSucesores(state, turn):
    global nodosGeneradosMM
    global nodosExpandidosMM
    nodosExpandidosMM = nodosExpandidosMM + 1
    newStates = []
    if(turn):                       #juegan blancas
        for pos in state.listaBlancas:
            states = Utils.getStates(pos[0],pos[1],state)
            nodosGeneradosMM = nodosGeneradosMM + len(states)
            newStates.extend(states)
    else:                           #juegan negras
        for pos in state.listaNegras:
            states = Utils.getStates(pos[0], pos[1], state)
            nodosGeneradosMM = nodosGeneradosMM + len(states)
            newStates.extend(states)
    return newStates






def MiniMax (state, turn):
    if turn:
        v, m = MinValue(state, turn, None)
        return v, m, nodosGeneradosMM, nodosExpandidosMM
    else:
        v, m = MaxValue(state, turn, None)
        return v, m, nodosGeneradosMM, nodosExpandidosMM



def MinValue(state, turn,m):
    turn = (turn+1)%2
    if state.isFinal or state.profundidad == 0:
        m = state.move
        return state.Utilidad(), m
    v = 1000000
    for st in getSucesores(state, turn):
        act_v = MaxValue(st, turn,m)[0]
        if act_v<v:
            v = act_v
            m = st.move

    return v,m
def MaxValue(state, turn,m):
    turn = (turn+1)%2
    if state.isFinal or state.profundidad == 0:
        m = state.move
        return state.Utilidad(), m
    v = -10000000
    for st in getSucesores(state, turn):
        act_v = MinValue(st, turn,m)[0]
        if act_v>v:
            v = act_v
            m = st.move

    return v,m


