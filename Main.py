# main to test the methods
import sys
import time

import Utils
from AlfaBeta import AlfaBeta
from MinMax import MiniMax
from Position import Position

if __name__ == '__main__':

    def makeMovement(state, turn, prof):
        if turn:
            i = 1
            for pos in state.listaBlancas:
                valuePiece = state.m_board[pos[0]][pos[1]]
                pieza = Utils.piezaFactory(state.m_board[pos[0]][pos[1]])
                state.m_agentPos = Position(pos[0], pos[1])
                if(len(pieza.getPossibleActions(state)) > 0):
                    print(str(i)+ ": Mover "+str(Utils.valueNames[valuePiece])+" en ["+str(pos[0]) + "," + str(pos[1])+"]"  )
                    i = i+1

            opt = int(input("Selecciona una pieza: "))
            posPiezaElegida = state.listaBlancas[opt - 1]
            state.m_agentPos = Position(posPiezaElegida[0], posPiezaElegida[1])
            pieza = Utils.piezaFactory(state.m_board[posPiezaElegida[0]][posPiezaElegida[1]])
            posibleActions = (pieza.getPossibleActions(state))
            i = 1
            for action in posibleActions:
                print(str(i) + ": Mover a " +str(action.m_finalPos) )
                i = i + 1
            act = int(input("Selecciona una accion: "))
            state = state.applyAction(posibleActions[act-1])
            state.profundidad = prof
            Utils.printBoard(state)
            return state

        else:
            i = 1
            for pos in state.listaNegras:
                valuePiece = state.m_board[pos[0]][pos[1]]
                pieza = Utils.piezaFactory(state.m_board[pos[0]][pos[1]])
                state.m_agentPos = Position(pos[0], pos[1])
                if(len(pieza.getPossibleActions(state)) > 0):
                    print(str(i)+ ": Mover "+str(Utils.valueNames[valuePiece])+" en ["+str(pos[0]) + "," + str(pos[1])+"]"  )
                    i = i+1
            opt = int(input("Selecciona una pieza: "))
            posPiezaElegida = state.listaNegras[opt - 1]
            state.m_agentPos = Position(posPiezaElegida[0], posPiezaElegida[1])
            pieza = Utils.piezaFactory(state.m_board[posPiezaElegida[0]][posPiezaElegida[1]])
            posibleActions = (pieza.getPossibleActions(state))
            i = 1
            for action in posibleActions:
                print(str(i) + ": Mover a " +str(action.m_finalPos) )
                i = i + 1
            act = int(input("Selecciona una accion: "))
            state = state.applyAction(posibleActions[act-1])
            state.profundidad = prof
            Utils.printBoard(state)
            return state


    def AIvsAI(maxMoves, seed, turn, prob, initial, prof, method):
        if (initial):
            st = Utils.getChessInstance(prob, seed, turn, prof)
        else:
            st = Utils.getChessInstancePosition(prob, seed, turn, prof)
        st.crearListas()
        Utils.printBoard(st)
        print("--------------------------------\n\n\n")
        final = False
        while maxMoves >0 and not final:
            if (method == "alphabeta"):
                v, m, gen, exp = (AlfaBeta(st, turn))
            else:
                v, m, gen, exp = (MiniMax(st, turn))
            print(f"Turn is {turn}")
            print(f"Evaluation value is {v}")
            print(f"Action is ${m} " + str(st.isFinal))

            st = st.applyAction(m)
            st.profundidad = prof
            if (st.isFinal):
                final = True
            Utils.printBoard(st)
            print(f"-----------------------------------\n\n\n")
            turn = (turn+1)%2
            maxMoves = maxMoves - 1

        if (v > 0):
            print("Ganan Blancas")
        elif (v < 0):
            print("Ganan Negras")
        else:
            print("Tablas")
        print(f"Generados: {gen}")
        print(f"Expandidos: {exp}")



    def humanvsAI(seed, turn, prob, initial, prof, method):

        if (initial):
            st = Utils.getChessInstance(prob, seed, turn, prof)
        else:
            st = Utils.getChessInstancePosition(prob, seed, turn, prof)
        st.crearListas()
        print(f"INITIAL")
        Utils.printBoard(st)
        print("--------------------------------\n\n\n")
        final = False
        while not final:
            #turno jugador
            st = makeMovement(st, turn, prof)
            if (st.isFinal):
                print("Humano gana")
                break
            #turno maquina
            if (method == "alphabeta"):
                v, m, gen, exp = (AlfaBeta(st, turn))
            else:
                v, m, gen, exp = (MiniMax(st, turn))
            print(f"Evaluation value is {v}")
            print(f"Action is ${m}")
            st = st.applyAction(m)
            if (st.isFinal):
                final = True
            st.profundidad = prof
            Utils.printBoard(st)
            print(f"-----------------------------\n\n\n")



    #humanvsAI(927, 0, 0.1, True, 3)
    #AIvsAI(100, 123123, 0, 0.1, False, 3, "alphabeta" )



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
        humanvsAI(seed, 0, prob, initial, profundidad, method)

    elif (color == "black"):
        humanvsAI(seed, 1, prob, initial, profundidad, method)

    elif (color == "todo"):
        whoStarts = int(sys.argv[8])
        print(initial)
        AIvsAI(maxJugadas, seed, whoStarts, prob, initial, profundidad, method)

    elif (color == "dummy"):
        pass

    end = time.time()
    print(f"Tiempo total {round(end - start, 4)} segundos")



