# main to test the methods
import Utils
from MinMax import MiniMax
import os
if __name__ == '__main__':
    welcomeS = "MINIMAX TEST MENU OPTIONS" \
               "\n1-Human vs algo" \
               "\n5-Exit sim" \
               "\n--------------------------"
    probS = "Select probability" \
            "\n2-0.2" \
            "\n3-0.3"
    thisdict = {
        1: "Human vs algo",
        2: "EXIT"
    }
    prob = {
        0: "Select probability (default)",
        2: "0.2",
        3: "0.3"
    }
    def getInteger():
        ok = False
        num = 0
        while not ok:
            try:
                num = int(input("Insert option\n"))
                ok = True
            except ValueError:
                print("Remember, only integers!")
        return num


    def menu(options, header):
        exited= False
        ext_str="EXIT"
        while not exited:
            print(header)
            opt = getInteger()
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
    myOpt = menu(thisdict, welcomeS)
    if myOpt==1:
        newOpt = float(menu(prob, probS))
        print(f"Selected probability is {newOpt}\n")
        st = Utils.getChessInstancePosition(newOpt, 100, 0)
        print(st.m_board)
        st.reloadPositions()
        Utils.printBoard(st)
        v, m = (MiniMax(st, 0))
        print(f"Evaluation value is {v}")
        print(f"Action is ${m}")

