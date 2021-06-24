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





def AlfaBeta (state, controlJuego):
    alfa = -1000000
    beta = 1000000
    if controlJuego:
        #juegan blancas
        v, m = MinValue(state, controlJuego, None, alfa, beta)
        return v, m, nodosGeneradosAB, nodosExpandidosAB
    else:
        #juegan negras
        v, m = MaxValue(state, controlJuego, None, alfa, beta)
        return v, m, nodosGeneradosAB, nodosExpandidosAB



def MinValue(state, turno, movimiento, alfa, beta):
    turno = (turno+1)%2
    if state.isFinal or state.profundidad == 0:
        movimiento = state.move
        return state.Utilidad(), movimiento
    v = 1000000
    for st in Sucesores(state,turno):
        valueV = MaxValue(st, turno,movimiento, alfa, beta)[0]
        if valueV < v:
            #igual que Min(v, MaxValue), pero permite coger el movimiento
            v = valueV
            movimiento = st.move
        if v <= alfa:
            return v, movimiento
        beta = min(v, beta)
    return v,movimiento


def MaxValue(state, turno,movimiento, alfa, beta):
    turno = (turno+1)%2
    if state.isFinal or state.profundidad == 0:
        movimiento = state.move
        return state.Utilidad(), movimiento
    v = -10000000
    for st in Sucesores(state, turno):
        valueV = MinValue(st, turno, movimiento, alfa, beta)[0]
        if valueV > v:
            #igual que Max(v, MinValue), pero permite coger el movimiento
            v = valueV
            movimiento = st.move
        if v >= beta:
            return v, movimiento
        alfa = max(v, alfa)
    return v,movimiento
