import Utils


nodosExpandidosAB = 0
nodosGeneradosAB = 0


def setToZeroExpandedAndGeneratedInAB():
    #pone a 0 expandidos y generados, usado en las pruebas
    global nodosGeneradosAB
    nodosGeneradosAB = 0
    global nodosExpandidosAB
    nodosExpandidosAB = 0

def Sucesores(state, jueganBlancas):
    global nodosGeneradosAB
    global nodosExpandidosAB
    nodosExpandidosAB = nodosExpandidosAB + 1

    estadosSucesores = []
    if(jueganBlancas):                       #juegan blancas
        for pos in state.listaBlancas:
            states = Utils.getStates(pos[0],pos[1],state)
            estadosSucesores.extend(states)
            nodosGeneradosAB = nodosGeneradosAB + (len(states))

    else:                           #juegan negras
        for pos in state.listaNegras:
            states = Utils.getStates(pos[0], pos[1], state)
            estadosSucesores.extend(states)
            nodosGeneradosAB = nodosGeneradosAB + (len(states))

    return estadosSucesores





def AlfaBeta (state, turn):
    alfa = -1000000
    beta = 1000000
    if turn:
        v, m = MinValue(state, turn, None, alfa, beta)
        return v, m, nodosGeneradosAB, nodosExpandidosAB
    else:
        v, m = MaxValue(state, turn, None, alfa, beta)
        return v, m, nodosGeneradosAB, nodosExpandidosAB



def MinValue(state, turn,m, alfa, beta):
    turn = (turn+1)%2
    if state.isFinal or state.profundidad == 0:
        m = state.move
        return state.Utilidad(), m
    v = 1000000
    for st in Sucesores(state,turn):
        act_v = MaxValue(st, turn,m, alfa, beta)[0]
        if act_v<v:
            v = act_v
            m = st.move
        if v <= alfa:
            return v, m
        beta = min(v, beta)
    return v,m


def MaxValue(state, turn,m, alfa, beta):
    turn = (turn+1)%2
    if state.isFinal or state.profundidad == 0:
        m = state.move
        return state.Utilidad(), m
    v = -10000000
    for st in Sucesores(state, turn):
        act_v = MinValue(st, turn,m, alfa, beta)[0]
        if act_v>v:
            v = act_v
            m = st.move
        if v >= beta:
            return v, m
        alfa = max(v, alfa)
    return v,m
