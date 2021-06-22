import Utils
from MiniMax import minimax
from Position import Position


def getStatePredefined(prob, seed, turn):
    state = Utils.get_chess_instance_position(prob, seed, turn)
    return state


def AIvsAI(maxMoves, seed, turn, prob, initial, prune=False):
    if (initial):
        st = Utils.get_chess_instance(prob, seed, turn)
    else:
        st = getStatePredefined(prob, seed, turn)
    st.reloadPositions()
    print(f"INITIAL")
    Utils.print_board(st)
    print("--------------------------------\n\n\n")
    final = False
    while maxMoves > 0 and not final:
        v, m, gen, exp = (minimax(st, turn, pruning=prune))
        print(f"Turn is {turn}")
        print(f"Evaluation value is {v}")
        print(f"Action is ${m}")
        if (st.m_board[m.m_finalPos.row][m.m_finalPos.col] == 5 or st.m_board[m.m_finalPos.row][
            m.m_finalPos.col] == 11):
            final = True
        st = st.applyAction(m)
        st.depth = 3
        Utils.print_board(st)
        print(f"--------------{maxMoves}---------------\n\n\n")
        turn = (turn + 1) % 2
        maxMoves = maxMoves - 1

    if (v > 0):
        print("Ganan Blancas")
    elif (v < 0):
        print("Ganan Negras")
    else:
        print("Tablas")
    print(f"Generados: {gen}")
    print(f"Expandidos: {exp}")


def makeMovement(state, turn):
    if turn:
        i = 1
        for pos in state.wElemList:
            valuePiece = state.m_board[pos[0]][pos[1]]
            print(str(i) + ": Mover " + str(Utils.valueNames[valuePiece]) + " en [" + str(pos[0]) + "," + str(
                pos[1]) + "]")
            i = i + 1

        opt = int(input("Selecciona una pieza: "))
        posPiezaElegida = state.wElemList[opt - 1]
        state.m_agentPos = Position(posPiezaElegida[0], posPiezaElegida[1])
        pieza = Utils.piece_factory(state.m_board[posPiezaElegida[0]][posPiezaElegida[1]])
        print(pieza.get_possible_actions(state))
        posibleActions = (pieza.get_possible_actions(state))
        i = 1
        for action in posibleActions:
            print(str(i) + ": Mover a " + str(action.m_finalPos))
            i = i + 1
        act = int(input("Selecciona una accion: "))
        state = state.applyAction(posibleActions[act - 1])
        state.depth = 3
        Utils.print_board(state)
        return state

    else:
        i = 1
        for pos in state.bElemList:
            valuePiece = state.m_board[pos[0]][pos[1]]
            print(str(i) + ": Mover " + str(Utils.valueNames[valuePiece]) + " en [" + str(pos[0]) + "," + str(
                pos[1]) + "]")
            i = i + 1
        opt = int(input("Selecciona una pieza: "))
        posPiezaElegida = state.bElemList[opt - 1]
        state.m_agentPos = Position(posPiezaElegida[0], posPiezaElegida[1])
        pieza = Utils.piece_factory(state.m_board[posPiezaElegida[0]][posPiezaElegida[1]])
        posibleActions = (pieza.get_possible_actions(state))
        i = 1
        for action in posibleActions:
            print(str(i) + ": Mover a " + str(action.m_finalPos))
            i = i + 1
        act = int(input("Selecciona una accion: "))
        state = state.applyAction(posibleActions[act - 1])
        state.depth = 3
        Utils.print_board(state)
        return state
        a = 0


def humanvsAI(seed, turn, prob, initial, prune=False):
    if (initial):
        st = Utils.get_chess_instance(prob, seed, turn)
    else:
        st = getStatePredefined(prob, seed, turn)
    st.reloadPositions()
    print(f"INITIAL")
    Utils.print_board(st)
    print("--------------------------------\n\n\n")
    final = False
    while not final:
        # turno jugador
        st = makeMovement(st, turn)
        if (st.isFinal):
            print("Humano gana")
            break
        # turno agente
        v, m, gen, exp = (minimax(st, turn, pruning=prune))
        print(f"Evaluation value is {v}")
        print(f"Action is ${m}")
        if (st.m_board[m.m_finalPos.row][m.m_finalPos.col] == 5 or st.m_board[m.m_finalPos.row][
            m.m_finalPos.col] == 11):
            final = True
        st = st.applyAction(m)
        st.depth = 3
        Utils.print_board(st)
        print(f"-----------------------------\n\n\n")
    print(f"Generados: {gen}")
    print(f"Expandidos: {exp}")


if __name__ == '__main__':
    # humanvsAI(927, 0, 0.1, False)
    AIvsAI(100, 123, 0, 0.2, False, True)
