# main to test the methods
import Utils
from MinMax import MiniMax
import os
if __name__ == '__main__':
    welcomeS = "MINIMAX TEST MENU OPTIONS" \
               "\n1-Human vs algo" \
               "\n5-Exit sim" \
               "\n--------------------------"
    mainMenu = {
        1: "Human vs algo",
        2: "EXIT"
    }
    def getFloat(start, end):
        ok = False
        num = 0
        while not ok:
            try:
                num = float(input(f"Insert probability betweeen {start} and {end}\n"))
                if num in [x * .1 for x in range(11)]:
                    ok = True
            except ValueError:
                print(f"Remember, only floats betweeen {start} and {end}!")
        return num


    def getInteger(warning):
        ok = False
        num = 0
        while not ok:
            try:
                num = int(input("Insert option\n"))
                ok = True
            except ValueError:
                print(f"Remember, {warning}!")
        return num

    def getStatePredefined():
        state = Utils.getChessInstancePosition(0, 3, 1)
        state.m_board[2][7] = 10
        state.m_board[4][7] = 10

        return state


    def menu(options, header):
        exited= False
        ext_str="EXIT"
        while not exited:
            print(header)
            opt = getInteger('only integers')
            if opt in options:
                if options[opt] == ext_str:
                    exited = True
                else:
                    print(f"{options[opt]} selected\n")
                    return opt
            else:
                print(f"Valid choices: {options}")
        print("END")
    ####################WORK FROM THIS POINT##########################
    #optIn = menu(mainMenu, welcomeS)
    optIn = 1
    if optIn==1:
        #prob = getFloat(0,1)
        #print(f"Selected probability is {prob}\n")
        #st = Utils.getChessInstancePosition(prob, 100, 0)
        st = getStatePredefined()
        print(st.m_board)
        st.reloadPositions()
        Utils.printBoard(st)
        v, m = (MiniMax(st, st.turn))
        print(f"Evaluation value is {v}")
        print(f"Action is ${m}")

