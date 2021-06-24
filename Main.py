import sys
import time

import Utils
from AlfaBeta import AlfaBeta
from MinMax import MiniMax
from Position import Position

if __name__ == '__main__':

    def makeMovement(state, turn, prof):
        if turn:
            accionSeleccionada = False
            while not accionSeleccionada:

                print("Piezas disponibles")
                i = 1
                for pos in state.listaBlancas:
                    valuePiece = state.m_board[pos[0]][pos[1]]
                    print(str(i)+ ": Mover "+str(Utils.valueNames[valuePiece])+" en ["+str(pos[0]) + "," + str(pos[1])+"]"  )
                    i = i+1

                opt = int(input("Selecciona una pieza: "))
                posPiezaElegida = state.listaBlancas[opt - 1]
                state.m_agentPos = Position(posPiezaElegida[0], posPiezaElegida[1])
                pieza = Utils.obtenerPieza(state.m_board[posPiezaElegida[0]][posPiezaElegida[1]])
                posibleActions = (pieza.getPossibleActions(state))
                if len(posibleActions) == 0:
                    print("Esta pieza no tiene movimientos disponibles")
                else:
                    i = 1
                    for action in posibleActions:
                        print(str(i) + ": Mover a " +str(action.m_finalPos) )
                        i = i + 1
                    act = int(input("Selecciona una accion: "))
                    if act >0 and act <= len(posibleActions):
                        accionSeleccionada = True

            state = state.applyAction(posibleActions[act-1])
            state.profundidad = prof
            Utils.printBoard(state)
            return state

        else:
            accionSeleccionada = False
            while not accionSeleccionada:
                print("Piezas disponibles")
                i = 1
                for pos in state.listaNegras:
                    valuePiece = state.m_board[pos[0]][pos[1]]
                    print(str(i)+ ": Mover "+str(Utils.valueNames[valuePiece])+" en ["+str(pos[0]) + "," + str(pos[1])+"]"  )
                    i = i+1
                opt = int(input("Selecciona una pieza: "))
                posPiezaElegida = state.listaNegras[opt - 1]
                state.m_agentPos = Position(posPiezaElegida[0], posPiezaElegida[1])
                pieza = Utils.obtenerPieza(state.m_board[posPiezaElegida[0]][posPiezaElegida[1]])
                posibleActions = (pieza.getPossibleActions(state))
                if len(posibleActions) == 0:
                    print("Esta pieza no tiene movimientos disponibles")
                else:
                    i = 1
                    for action in posibleActions:
                        print(str(i) + ": Mover a " +str(action.m_finalPos) )
                        i = i + 1
                    act = int(input("Selecciona una accion: "))
                    if act > 0 and act <= len(posibleActions):
                        accionSeleccionada = True

            state = state.applyAction(posibleActions[act-1])
            state.profundidad = prof
            Utils.printBoard(state)
            return state


    def MaquinaVsMaquina(maxMoves, seed, jueganBlancas, prob, initial, prof, method):
        if (initial):
            st = Utils.getChessInstance(prob, seed, jueganBlancas, prof)
        else:
            st = Utils.getChessInstancePosition(prob, seed, jueganBlancas, prof)
        st.crearListas()
        Utils.printBoard(st)
        print("--------------------------------\n\n\n")
        final = False
        while maxMoves >0 and not final:
            if (method == "alphabeta"):
                v, m, gen, exp = (AlfaBeta(st, jueganBlancas))
            else:
                v, m, gen, exp = (MiniMax(st, jueganBlancas))
            print("v = " + str(v) + "  Accion seguida => " + str(m))

            st = st.applyAction(m)
            st.profundidad = prof
            if (st.isFinal):
                final = True
            Utils.printBoard(st)
            print(f"-----------------------------------\n\n\n")
            jueganBlancas = (jueganBlancas+1)%2
            maxMoves = maxMoves - 1

        if (v > 0):
            print("Ganan Blancas")
        elif (v < 0):
            print("Ganan Negras")
        else:
            print("Tablas")
        print(f"Generados: "+str(gen))
        print(f"Expandidos: "+str(exp))



    def humanvsAI(seed, jueganBlancas, prob, initial, prof, method, dummy):

        if (initial):
            st = Utils.getChessInstance(prob, seed, jueganBlancas, prof)
        else:
            st = Utils.getChessInstancePosition(prob, seed, jueganBlancas, prof)
        st.crearListas()
        Utils.printBoard(st)
        print("--------------------------------\n\n\n")
        final = False
        while not final:
            #turno jugador
            if dummy:
                print("Humano es Dummy y no juega")
            else:
                if not jueganBlancas:
                    print("Juegan negras (Humano)" + str(jueganBlancas))
                else:
                    print("Juegan blancas (Humano)" + str(jueganBlancas))
                st = makeMovement(st, jueganBlancas, prof)
                if (st.isFinal):
                    print("Humano gana")
                    break
            #turno maquina
            print("\n\n\n\n\n\n")
            if jueganBlancas:
                print("Juegan negras (Maquina)" + str(jueganBlancas))
            else:
                print("Juegan blancas (Maquina)" + str(jueganBlancas))

            if (method == "alphabeta"):
                v, m, gen, exp = (AlfaBeta(st, jueganBlancas))
            else:
                v, m, gen, exp = (MiniMax(st, jueganBlancas))

            print("v = " + str(v) + "  Accion seguida => " + str(m))
            st = st.applyAction(m)
            if (st.isFinal):
                final = True
                print("Gana la Maquina")
            st.profundidad = prof
            Utils.printBoard(st)
            print(f"-----------------------------\n\n\n")





    method = str(sys.argv[1])
    inicio = str(sys.argv[2])
    profundidad = int(sys.argv[3])
    color = str(sys.argv[4])
    maxJugadas = int(sys.argv[5])
    prob = float(sys.argv[6])
    seed = int(sys.argv[7])

    if (inicio == "False"):
        initial = False
    if (inicio == "True"):
        initial = True

    start = time.time()


    if (color == "white"):
        print("White enemy")
        humanvsAI(seed, 0, prob, initial, profundidad, method, False)

    elif (color == "black"):
        humanvsAI(seed, 1, prob, initial, profundidad, method, False)

    elif (color == "todo"):
        whoStarts = int(sys.argv[8])
        print(initial)
        MaquinaVsMaquina(maxJugadas, seed, whoStarts, prob, initial, profundidad, method)

    elif (color == "dummy"):
        humanvsAI(seed, 1, prob, initial, profundidad, method, True)

    end = time.time()
    print(f"Tiempo total {round(end - start, 4)} segundos")
    #end
