import sys
from MinMax import MiniMax
from AlfaBeta import AlfaBeta
from MinMax import setToZeroExpandedAndGeneratedInMM
from AlfaBeta import setToZeroExpandedAndGeneratedInAB
import time
import Utils
#pruebasar
methods = ["minmax", "alphabeta"]
seeds = [76, 234, 345, 456, 567, 678, 789, 890, 901, 1045]
tiempos = []
nodosAlphaBeta = []
nodosMinimax =[]
nPiezas = []
movementsAlphaBeta = []
movementsMinMax = []
timeMinMax = []
timeAlphabeta = []
def createDefinedStates():
    states = []
    st1 = Utils.getChessInstancePosition(0, 6, 0, 3)
    st2 = Utils.getChessInstancePosition(0, 6, 0, 3)
    st3 = Utils.getChessInstancePosition(0, 6, 0, 3)
    st4 = Utils.getChessInstancePosition(0, 6, 0, 3)

    #predef for St1
    st1.m_board[7][5] =Utils.bRook
    st1.m_board[6][5] =Utils.bPawn
    st1.m_board[6][6] =Utils.bPawn
    st1.m_board[6][7] =Utils.bPawn

    st1.m_board[5][6] =Utils.wQueen


    #predef for st2
    st2.m_board[6][7] =Utils.bPawn
    st2.m_board[6][6] =Utils.bPawn
    st2.m_board[7][6] =Utils.bPawn

    st2.m_board[0][0] = Utils.wRook
    st2.m_board[0][3] = Utils.wRook

    st2.m_board[6][0] = Utils.bQueen
    st2.m_board[6][3] = Utils.bRook

    #predef for st3
    st3.m_board[6][7] =Utils.bPawn
    st3.m_board[6][6] =Utils.bPawn
    st3.m_board[7][6] =Utils.bPawn

    st3.m_board[0][1] = Utils.bRook
    st3.m_board[0][3] = Utils.bRook

    #predef for st4
    st4.m_board[6][7] =Utils.bPawn
    st4.m_board[6][6] =Utils.bPawn
    st4.m_board[7][6] =Utils.bPawn

    st4.m_board[0][1] = Utils.bQueen
    st4.m_board[0][3] = Utils.bRook
    st4.m_board[7][2] = Utils.bRook

    #Utils.printBoard(st3)
    states.append(st1)
    states.append(st2)
    states.append(st3)
    states.append(st4)

    return states








#prueba = 2
#indexPrueba = 3
prueba = int(sys.argv[1])
if prueba == 1:
    indexPrueba = int(sys.argv[2])
    if (indexPrueba == 5):
        for a in range(4):
            print("Prueba " + str(a+1))
            listaPruebasPredefinidas = createDefinedStates()
            state = listaPruebasPredefinidas[a]
            state.crearListas()
            Utils.printBoard(state)
            v, m, gen, exp = (AlfaBeta(state, 0))
            st = state.applyAction(m)
            Utils.printBoard(st)
            print("------------------------------------------")
    else:
        print("Prueba " + str(indexPrueba))
        listaPruebasPredefinidas = createDefinedStates()
        state = listaPruebasPredefinidas[indexPrueba - 1]
        state.crearListas()
        Utils.printBoard(state)
        v, m, gen, exp = (AlfaBeta(state, 0))
        st = state.applyAction(m)
        Utils.printBoard(st)
        print("------------------------------------------")

elif prueba == 2:
    prob = float(sys.argv[2])
    prof = int(sys.argv[3])
    #prob = 0.2
    #prof = 2
    for method in methods:
        print("Ejecutando " + method)
        for i in range(10):
            print("Prueba "+str(i+1))


            if (method == "alphabeta"):
                st = Utils.getChessInstancePosition(prob, seeds[i], 0, prof)
                st.crearListas()
                Utils.printBoard(st)
                startPrueba = time.time()
                v, m, gen, exp = (AlfaBeta(st, 0))
                endPrueba = time.time()
                nodosAlphaBeta.append((gen, exp))
                setToZeroExpandedAndGeneratedInAB()
                nPiezas.append(len(st.listaNegras) + len(st.listaBlancas))
                movementsAlphaBeta.append(m)
                timeAlphabeta.append({round(endPrueba - startPrueba, 4)})

            else:
                st = Utils.getChessInstancePosition(prob, seeds[i], 0, prof)
                st.crearListas()
                Utils.printBoard(st)
                startPrueba = time.time()
                v, m, gen, exp = (MiniMax(st, 0))
                endPrueba = time.time()
                nodosMinimax.append((gen, exp))
                setToZeroExpandedAndGeneratedInMM()
                movementsMinMax.append(m)
                timeMinMax.append({round(endPrueba - startPrueba, 4)})

    print("Prueba. \tNGMinMax\tNEMinMax\tNGAlpBet\tNEAlpBet\tAccion tomada en MiniMax\tAccion tomada en AlfaBeta\tN.Piezas\tT. MiniMax\tT. Alfabeta")
    for a in range(10):
        tMM = timeMinMax[a].pop()
        tAB = timeAlphabeta[a].pop()

        print("Prueba" + str(a) +"\t\t"+str(nodosMinimax[a][0])+"\t\t"+str(nodosMinimax[a][1])+"\t\t"+str(nodosAlphaBeta[a][0]) + "\t\t"+str(nodosAlphaBeta[a][1])+"\t\t"+str(movementsMinMax[a])+"\t\t"+str(movementsAlphaBeta[a])+"\t\t" + str(nPiezas[a]) + "\t\t"+str(tMM)+"sec"+"\t"+str(tAB)+"sec")

elif prueba == 3:
    # prof 2 => 9 pasos
    #prof 3 => 7 pasos
    #seed = 1233
    #seed = 6344
    #seed = 7463
    #prof = 2
    seed = int(sys.argv[2])
    prof = int(sys.argv[3])
    st1 = Utils.getChessInstancePosition(0.2, seed, 0, prof)
    st2 = Utils.getChessInstancePosition(0.2, seed, 0, prof + 1)
    st3 = Utils.getChessInstancePosition(0.2, seed, 0, prof + 2)




    st1.crearListas()
    st2.crearListas()
    st3.crearListas()
    Utils.printBoard(st1)


    final = False
    turn = 1
    pasos1 = 0
    maxMovimientos = 100
    listaAcciones1 = []
    while  not final and maxMovimientos >0:
        pasos1 += 1
        v, m, gen, exp = (AlfaBeta(st1, turn))
        print("v = " + str(v) + "  Accion seguida => " + str(m))
        st1 = st1.applyAction(m)
        listaAcciones1.append(m)
        st1.profundidad = prof
        if (st1.isFinal):
            final = True
        Utils.printBoard(st1)
        print(f"-----------------------------------\n\n\n")
        turn = (turn + 1) % 2
        maxMovimientos = maxMovimientos -1
        print(pasos1)
    print("***************************************")
    print(pasos1)
    final = False
    turn = 1
    pasos2 = 0
    Utils.printBoard(st2)
    listaAcciones2 = []

    while  not final:
        pasos2 += 1
        v, m, gen, exp = (AlfaBeta(st2, turn))
        print("v = " + str(v) + "  Accion seguida => " + str(m))
        st2 = st2.applyAction(m)
        listaAcciones2.append(m)

        st2.profundidad = prof + 1
        if (st2.isFinal):
            final = True
        Utils.printBoard(st2)
        print(f"-----------------------------------\n\n\n")
        turn = (turn + 1) % 2
        print(pasos2)
    print("***************************************")

    final = False
    turn = 1
    pasos3 = 0
    Utils.printBoard(st3)
    listaAcciones3 = []

    while  not final:
        pasos3 += 1
        v, m, gen, exp = (AlfaBeta(st3, turn))
        print("v = " + str(v) + "  Accion seguida => " + str(m))
        st3 = st3.applyAction(m)
        listaAcciones3.append(m)
        st3.profundidad = prof + 2
        if (st3.isFinal):
            final = True
        Utils.printBoard(st3)
        print(f"-----------------------------------\n\n\n")
        turn = (turn + 1) % 2
        print(pasos3)
    print("Problema 1 con profundidad = "+str(prof)+"Numero de acciones = " + str(pasos1))
    for accion in listaAcciones1:
        print(accion)
    print("Problema 1 con profundidad = "+str(prof + 1)+"Numero de acciones = " + str(pasos2))
    for accion in listaAcciones2:
        print(accion)
    print("Problema 1 con profundidad = "+str(prof + 2)+"Numero de acciones = " + str(pasos3))
    for accion in listaAcciones3:
        print(accion)
#print(nodosAlphaBeta)