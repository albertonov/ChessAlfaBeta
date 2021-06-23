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
    if turn:
        i = 1
        for pos in state.wElemList:
            value_piece = state.m_board[pos[0]][pos[1]]
            print(str(i) + f"{i}: Move {Utils.valueNames[value_piece]} to [{pos[0]},{pos[0]}]")
            i = i + 1
        opt = int(input("Select a piece to move: "))
        pos_selected = state.wElemList[opt - 1]
        state.m_agentPos = Position(pos_selected[0], pos_selected[1])
        piece = Utils.piece_factory(state.m_board[pos_selected[0]][pos_selected[1]])
        print(piece.get_possible_actions(state))
        possible_actions = (piece.get_possible_actions(state))
        i = 1
        for action in possible_actions:
            print(f"{i}: Move to position {action.m_finalPos}")
            i = i + 1
        act = int(input("Which action?"))
        state = state.applyAction(possible_actions[act - 1])
        state.depth = depth
        Utils.print_board(state)
        return state
    else:
        i = 1
        for pos in state.bElemList:
            value_piece = state.m_board[pos[0]][pos[1]]
            print(str(i) + f"{i}: Move {Utils.valueNames[value_piece]} to [{pos[0]},{pos[0]}]")
            i = i + 1
        opt = int(input("Select a piece to move: "))
        pos_selected = state.bElemList[opt - 1]
        state.m_agentPos = Position(pos_selected[0], pos_selected[1])
        piece = Utils.piece_factory(state.m_board[pos_selected[0]][pos_selected[1]])
        possible_actions = (piece.get_possible_actions(state))
        i = 1
        for action in possible_actions:
            print(f"{i}: Move to position {action.m_finalPos}")
            i = i + 1
        act = int(input("Which action?"))
        state = state.applyAction(possible_actions[act - 1])
        state.depth = depth
        Utils.print_board(state)
        return state


def human_vs_ai(seed, turn, prob, initial, prune=False, depth=3):
    if initial:
        st = Utils.get_chess_instance(prob, seed, turn)
    else:
        st = get_test_state(prob, seed, turn)
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
    stats.finalize()
    stats.show_me()


if __name__ == '__main__':
    # human_vs_ai(927, 0, 0.1, False)
    ai_vs_ai(100, 123, 0, 0.2, False, True)
