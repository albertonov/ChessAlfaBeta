import Utils
from MiniMax import minimax
from Position import Position

LINE_LENGTH = 27
moves = 0


def get_test_state(prob, seed, turn):
    state = Utils.get_chess_instance_position(prob, seed, turn)
    return state


def ai_vs_ai(max_moves, seed, turn, prob, initial, prune=False, depth=3):
    if initial:
        st = Utils.get_chess_instance(prob, seed, turn)
    else:
        st = get_test_state(prob, seed, turn)
    st.reloadPositions(depth)
    Utils.print_board(st)
    print('-' * LINE_LENGTH)
    final = False
    while max_moves > 0 and not final:
        v, m, stats = (minimax(st, turn, pruning=prune))
        print(f"Turn is {turn}")
        print(f"Evaluation value is {v}")
        print(f"Action is ${m}")
        if st.m_board[m.m_finalPos.row][m.m_finalPos.col] == 5 or st.m_board[m.m_finalPos.row][m.m_finalPos.col] == 11:
            final = True
        st = st.applyAction(m)
        st.depth = depth
        Utils.print_board(st)
        global moves
        moves = moves + 1
        print(f"------------{moves}--------------\n\n")
        turn = (turn + 1) % 2
        max_moves = max_moves - 1

    if (v > 0):
        print("Ganan Blancas")
    elif (v < 0):
        print("Ganan Negras")
    else:
        print("Tablas")
    print(f"Generados: {stats.generated}")
    print(f"Expandidos: {stats.expanded}")


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


def humanvsAI(seed, turn, prob, initial, prune=False, depth=3):
    if (initial):
        st = Utils.get_chess_instance(prob, seed, turn)
    else:
        st = get_test_state(prob, seed, turn)
    st.reloadPositions(depth)
    print('-' * LINE_LENGTH)
    Utils.print_board(st)
    print('-' * LINE_LENGTH)
    final = False
    while not final:
        # turno jugador
        st = makeMovement(st, turn)
        if (st.isFinal):
            print("Humano gana")
            break
        # turno agente
        v, m, stats = (minimax(st, turn, pruning=prune))
        print(f"Evaluation value is {v}")
        print(f"Action is ${m}")
        if (st.m_board[m.m_finalPos.row][m.m_finalPos.col] == 5 or st.m_board[m.m_finalPos.row][
            m.m_finalPos.col] == 11):
            final = True
        st = st.applyAction(m)
        st.depth = depth
        Utils.print_board(st)
        print('-' * LINE_LENGTH)
    print(f"Generados: {stats.expanded}")
    print(f"Expandidos: {stats.generated}")


if __name__ == '__main__':
    # humanvsAI(927, 0, 0.1, False)
    ai_vs_ai(100, 123, 0, 0.2, False, False)
