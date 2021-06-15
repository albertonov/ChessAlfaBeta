# main to test the methods
import Utils
from MinMax import MiniMax
import os
if __name__ == '__main__':


    def getStatePredefined(prob, seed, turn):
        state = Utils.getChessInstancePosition(prob, seed, turn)
        state.m_board[2][7] = 10
        state.m_board[4][7] = 10

        return state

    def AIvsAI(maxMoves, seed, turn, prob):
        st = getStatePredefined(prob, seed, turn)
        st.reloadPositions()
        print(f"INITIAL")
        Utils.printBoard(st)
        print("--------------------------------\n\n\n")
        final = False
        while maxMoves >0 or not final:
            v, m = (MiniMax(st, turn))
            print(f"Evaluation value is {v}")
            print(f"Action is ${m}")
            st = st.applyAction(m)
            Utils.printBoard(st)
            print(f"--------------{maxMoves}---------------\n\n\n")
            final = st.isFinal
            turn = (turn+1)%2
            maxMoves = maxMoves - 1
    AIvsAI(5, 3, 1, 0)

    '''
    st = getStatePredefined()
    print(st.m_board)
    st.reloadPositions()
    Utils.printBoard(st)
    v, m = (MiniMax(st, st.turn))
    print(f"Evaluation value is {v}")
    print(f"Action is ${m}")
    '''

