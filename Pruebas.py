import sys
from MinMax import MiniMax
from AlfaBeta import AlfaBeta
from MinMax import setToZeroExpandedAndGeneratedInMM
from AlfaBeta import setToZeroExpandedAndGeneratedInAB
import time
import Utils

methods = ["minmax", "alphabeta"]
seeds = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
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

else:
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
                nPiezas.append(len(st.bElemList) + len(st.wElemList))
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
    #print(nodosAlphaBeta)