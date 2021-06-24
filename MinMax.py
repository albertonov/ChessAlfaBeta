import Utils


nodosGeneradosMM = 0
nodosExpandidosMM = 0


def setToZeroExpandedAndGeneratedInMM():
    #pruebas
    global nodosGeneradosMM
    nodosGeneradosMM = 0
    global nodosExpandidosMM
    nodosExpandidosMM = 0

def getSucesores(state, jueganBlancas):
    #funcion que, dado un estado y el turno de un jugador, devuelve todos los nuevos estados posibles
    global nodosGeneradosMM
    global nodosExpandidosMM
    nodosExpandidosMM = nodosExpandidosMM + 1
    newStates = []
    if(jueganBlancas):
        for pos in state.listaBlancas:
            states = Utils.getStates(pos[0],pos[1],state)
            nodosGeneradosMM = nodosGeneradosMM + len(states)
            newStates.extend(states)
    else:
        for pos in state.listaNegras:
            states = Utils.getStates(pos[0], pos[1], state)
            nodosGeneradosMM = nodosGeneradosMM + len(states)
            newStates.extend(states)
    return newStates






def MiniMax (state, controlJuego):
    if controlJuego:
        #juegan blancas
        v, m = MinValue(state, controlJuego, None)
        return v, m, nodosGeneradosMM, nodosExpandidosMM
    else:
        #juegan negras
        v, m = MaxValue(state, controlJuego, None)
        return v, m, nodosGeneradosMM, nodosExpandidosMM



def MinValue(state, turno,movimiento):
    turno = (turno+1)%2
    if state.isFinal or state.profundidad == 0:
        movimiento = state.move
        return state.Utilidad(), movimiento
    v = 10000000
    for st in getSucesores(state, turno):
        valueV = MaxValue(st, turno, movimiento)[0]
        if valueV < v:
            #igual que Min(v, MaxValue), pero permite coger el movimiento
            v = valueV
            movimiento = st.move

    return v,movimiento

def MaxValue(state, turno,movimiento):
    turno = (turno+1)%2
    if state.isFinal or state.profundidad == 0:
        movimiento = state.move
        return state.Utilidad(), movimiento
    v = -10000000
    for st in getSucesores(state, turno):
        valueV = MinValue(st, turno,movimiento)[0]
        if valueV > v:
            #igual que Max(v, MinValue), pero permite coger el movimiento
            v = valueV
            movimiento = st.move

    return v,movimiento


