# main to test the methods
import Utils
from MinMax import MiniMax
import os
if __name__ == '__main__':


    def getStatePredefined(prob, seed, turn):
        state = Utils.getChessInstancePosition(prob, seed, turn)




        #state.m_board[4][7] = 10
        #state = Utils.getChessInstance(prob, seed, turn)
        return state

    def AIvsAI(maxMoves, seed, turn, prob):
        st = getStatePredefined(prob, seed, turn)
        st.reloadPositions()
        print(f"INITIAL")
        Utils.printBoard(st)
        print("--------------------------------\n\n\n")
        final = False
        while maxMoves >0 and not final:
            if (maxMoves == 47) :
                pass
            v, m = (MiniMax(st, turn))
            print(f"Turn is {turn}")
            print(f"Evaluation value is {v}")
            print(f"Action is ${m}")
            if (st.m_board[m.m_finalPos.row][m.m_finalPos.col] == 5  or st.m_board[m.m_finalPos.row][m.m_finalPos.col] == 11):
                final = True
            st = st.applyAction(m)
            st.depth = 3
            Utils.printBoard(st)
            print(f"--------------{maxMoves}---------------\n\n\n")
            turn = (turn+1)%2
            maxMoves = maxMoves - 1
    AIvsAI(50, 656, 1, 0.3)

    '''
    st = getStatePredefined()
    print(st.m_board)
    st.reloadPositions()
    Utils.printBoard(st)
    v, m = (MiniMax(st, st.turn))
    print(f"Evaluation value is {v}")
    print(f"Action is ${m}")
    '''

