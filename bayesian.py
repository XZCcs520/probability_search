import numpy as np
import random

def set_target(dim):
    return random.randrange(0, dim)

def random_board(dim):
    type_prob = [0.4, 0.3, 0.2, 0.1]
    board = np.random.choice(range(0, 4), size=(dim, dim), p=type_prob)
    belief = np.full([dim, dim], 1.0/dim/dim)
    #target = (set_target(dim), set_target(dim))
    target_row = set_target(dim)
    target_col = set_target(dim)
    return board, belief, target_row, target_col


def rule2_belief(board, belief, dim):
    P = [0.1, 0.3, 0.7, 0.9]
    ret = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            if belief[i][j] == 0:
                ret[i][j] = 0
            else:
                ret[i][j] = (1.0 - P[board[i][j]])/belief[i][j]
    return ret


def find_max_prob(belief, dim):
    max = -1
    col = 0
    row = 0
    for i in range(dim):
        for j in range(dim):
            if(belief[i][j] > max):
                max = belief[i][j]
                col = i
                row = j
    return col, row



def is_found(prob):
    tmp = set_target(100)
    #print tmp
    if tmp >= prob * 100:

        return True
    else:
        return False


def search_update(board, belief, target_row, target_col, dim, row, col):
    P = [0.1, 0.3, 0.7, 0.9] # P(Target not found in Cell[i]| Target is in Cell[i]), probability for flat, hill, forest, cave
    if target_row == row and target_col == col:
        if is_found(P[board[row][col]]) == False:
            belief[row][col] = 1.0 * P[board[row][col]] * belief[row][col] / (belief[row][col] + (1.0 - belief[row][col])) * P[board[row][col]]
            # update other cells
            for i in range(dim):
                # print belief
                for j in range(dim):
                    if i != row and j != col:
                        belief[i][j] = 1.0 * belief[i][j] / (belief[i][j] + (1.0 - belief[i][j]) * P[board[i][j]])
        else:
            return True
    else:
        belief[row][col] = 0.0
    return False


def rule1_solver(board_dim):
    board, belief, target_row, target_col = random_board(board_dim)
    print "board: "
    print board
    print "target position: "
    print target_row, target_col
    print "belief: "
    print belief
    # P(Target not found in Cell[i]| Target is in Cell[i]), probability for flat, hill, forest, cave
    P = [0.1, 0.3, 0.7, 0.9]
    # Implemented with Rule 1
    s_row = 0
    s_col = 0
    step = 0
    while True:
        step += 1
        s_row, s_col = find_max_prob(belief, board_dim)
        print "max prob point"
        print s_row, s_col
        flag = search_update(board, belief, target_row, target_col, board_dim, s_row, s_col)
        print "belief: "
        print belief
        if flag == True:
            break
    print "max step"
    return step


def rule2_solver(board_dim):
    board, belief, target_row, target_col = random_board(board_dim)
    print "board: "
    print board
    print "target position: "
    print target_row, target_col
    print "belief: "
    print belief
    belief_rule2 = rule2_belief(board, belief, board_dim)
    # P(Target not found in Cell[i]| Target is in Cell[i]), probability for flat, hill, forest, cave
    P = [0.1, 0.3, 0.7, 0.9]
    # Implemented with Rule 1
    s_row = 0
    s_col = 0
    step = 0
    while True:
        step += 1
        s_row, s_col = find_max_prob(belief_rule2, board_dim)
        print "max prob point"
        print s_row, s_col
        flag = search_update(board, belief, target_row, target_col, board_dim, s_row, s_col)
        belief_rule2 = rule2_belief(board, belief, board_dim)
        print "belief: "
        print belief
        if flag == True:
            break
    print "max step"
    return step


def __main():
    board_dim = int(input("Please enter a number indicating the dimension of grid: "))
    #cell_prob = float(input("Please enter a float number indicating the probability of flat terrain: "))
    #print rule1_solver(board_dim)
    print rule2_solver(board_dim)


__main()