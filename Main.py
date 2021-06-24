import sys
import Utils
from MiniMax import minimax
from Position import Position

LINE_LENGTH = 27
moves = 0


def get_test_state(prob, seed, turn):
    state = Utils.get_chess_instance_position(prob, seed, turn)
    return state


def ai_vs_ai(max_moves, seed, turn, prob, initial, prune=False, depth=3, test=0):
    if initial:
        st = Utils.get_chess_instance(prob, seed, turn)
    elif test == 0:
        st = get_test_state(prob, seed, turn)
    elif test == 1:
        st = get_test_state(prob, seed, turn)
        st.m_board[6][4] = Utils.wQueen
        #  st.m_board[5][7] = Utils.bQueen
    elif test == 2:
        st = get_test_state(prob, seed, turn)
        st.m_board[1][1] = Utils.bRook
        st.m_board[2][3] = Utils.wRook
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
        stats.total_moves = stats.total_moves + 1
        print(f"------------{stats.total_moves}--------------\n\n")
        turn = (turn + 1) % 2
        max_moves = max_moves - 1

    if v > 0:
        print("WHITES WIN!")
    elif v < 0:
        print("BLACKS WIN!")
    else:
        print("DRAW!")
    stats.finalize()
    stats.show_me()


def manual_move(state, turn, depth):
    unmovable = True
    if turn:
        i = 1
        for pos in state.wElemList:
            value_piece = state.m_board[pos[0]][pos[1]]
            print(f"{i}: Move {Utils.valueNames[value_piece]} located [{pos[0]},{pos[1]}]")
            i = i + 1
        opt = int(input("Select a piece to move: "))
        while unmovable:
            pos_selected = state.wElemList[opt - 1]
            state.m_agentPos = Position(pos_selected[0], pos_selected[1])
            piece = Utils.piece_factory(state.m_board[pos_selected[0]][pos_selected[1]])
            print(piece.get_possible_actions(state))
            possible_actions = (piece.get_possible_actions(state))
            i = 1
            for action in possible_actions:
                print(f"{i}: Move to position {action.m_finalPos}")
                i = i + 1
            if len(possible_actions) != 0:
                unmovable = False
                range_check = True
                while range_check:
                    act = int(input("Which action?"))
                    if act in range(1, len(possible_actions) + 1):
                        range_check = False
            else:
                print(f"The piece {Utils.valueNames[piece.m_type]} has no legal moves")
                opt = int(input("Select a different one: "))
        state = state.applyAction(possible_actions[act - 1])
        state.depth = depth
        Utils.print_board(state)
        return state
    else:
        i = 1
        for pos in state.bElemList:
            value_piece = state.m_board[pos[0]][pos[1]]
            print(f"{i}: Move {Utils.valueNames[value_piece]} located [{pos[0]},{pos[1]}]")
            i = i + 1
        opt = int(input("Select a piece to move: "))
        while unmovable:
            pos_selected = state.bElemList[opt - 1]
            state.m_agentPos = Position(pos_selected[0], pos_selected[1])
            piece = Utils.piece_factory(state.m_board[pos_selected[0]][pos_selected[1]])
            possible_actions = (piece.get_possible_actions(state))
            i = 1
            for action in possible_actions:
                print(f"{i}: Move to position {action.m_finalPos}")
                i = i + 1
            if len(possible_actions) != 0:
                unmovable = False
                range_check = True
                while range_check:
                    act = int(input("Which action?"))
                    if act in range(1, len(possible_actions)+1):
                        range_check = False
            else:
                print(f"The piece {Utils.valueNames[piece.m_type]} has no legal moves")
                opt = int(input("Select a different one: "))
        state = state.applyAction(possible_actions[act - 1])
        state.depth = depth
        Utils.print_board(state)
        return state


def human_vs_ai(seed, turn, prob, initial, prune=False, depth=3, ai_on=True, test=0):
    if initial:
        st = Utils.get_chess_instance(prob, seed, turn)
    elif test == 0:
        st = get_test_state(prob, seed, turn)
    elif test == 1:
        st = get_test_state(prob, seed, turn)
        st.m_board[6][4] = Utils.wQueen
        st.m_board[5][7] = Utils.bQueen
    st.reloadPositions(depth)
    print('-' * LINE_LENGTH)
    Utils.print_board(st)
    print('-' * LINE_LENGTH)
    final = False
    while not final:
        # manual move for human player
        st = manual_move(st, turn, depth)
        if st.isFinal:
            print("Human player wins!")
            break
        # AI turn
        if ai_on:
            v, m, stats = (minimax(st, turn, pruning=prune))
            print(f"Evaluation value is {v}")
            print(f"Action is ${m}")
            if (st.m_board[m.m_finalPos.row][m.m_finalPos.col] == 5 or st.m_board[m.m_finalPos.row][
                m.m_finalPos.col] == 11):
                final = True
            st = st.applyAction(m)
            st.depth = depth
            stats.total_moves = stats.total_moves + 1
        Utils.print_board(st)
        print('-' * LINE_LENGTH)
    if v > 0:
        print("WHITES WIN!")
    elif v < 0:
        print("BLACKS WIN!")
    else:
        print("DRAW!")
    stats.finalize()
    stats.show_me()


if __name__ == '__main__':
    print(f"Len reads {len(sys.argv)}")
    if len(sys.argv) not in [5, 9]:
        print(f"Arguments:")
        print(f"Initial config:------------")
        print(f"\t\t1. method (minimax/alphabeta)")
        print(f"\t\t2. initial (True/False)")
        print(f"\t\t3. depth (1-2-3-4-5, do not exceed!)")
        print(f"\t\t4. color (white/black/both/dummy)")
        print(f"\t\t5. probability (float between 0 and 1) optional")
        print(f"\t\t6. seed (any integer) optional")
        print(f"\t\t7. move_limit (1-any integer) optional")
        print(f"\t\t8. test cases(0,1,2,3) optional")
        sys.exit()
    in_method = str(sys.argv[1])
    in_initial = str(sys.argv[2])
    in_depth = int(sys.argv[3])
    in_color = str(sys.argv[4])
    in_probability = 0.2
    in_move_limit = 1000
    in_seed = 100
    in_test = 0
    if len(sys.argv) == 9:
        in_probability = float(sys.argv[5])
        in_seed = int(sys.argv[6])
        in_move_limit = int(sys.argv[7])
        in_test = int(sys.argv[8])
    in_prune = False
    if in_method == "alphabeta":
        in_prune = True
    if in_initial == "false":
        in_initial = False
    elif in_initial == "true":
        in_initial = True
    else:
        in_initial = False
        print(f"Defaulting to Non-complete configuration!")
    if in_test == 0:
        if in_color == "white":
            print(f"AI plays {in_color}")
            human_vs_ai(in_seed, 0, in_probability, in_initial, in_prune, in_depth)
        elif in_color == "black":
            human_vs_ai(in_seed, 1, in_probability, in_initial, in_prune, in_depth)
        elif in_color == "both":
            ai_vs_ai(in_move_limit, in_seed, 0, in_probability, in_initial, in_prune, in_depth)
        elif in_color == "dummy":
            human_vs_ai(in_seed, 0, in_probability, in_initial, in_prune, in_depth, False)
    elif in_color == "both":
        ai_vs_ai(in_move_limit, in_seed, 0, in_probability, in_initial, in_prune, in_depth, in_test)
