import numpy as np
import random
import sys


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
            ret[i][j] = (1 - P[board[i][j]]) * belief[i][j]

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


def update(board, belief, dim, row, col):
    P = [0.1, 0.3, 0.7, 0.9]  # P(Target not found in Cell[i]| Target is in Cell[i]), probability for flat, hill, forest, cave
    belief[row][col] = 1.0 * P[board[row][col]] * belief[row][col] / (P[board[row][col]] * belief[row][col] + 1.0 - belief[row][col])
    # update other cells
    for i in range(dim):
        # print belief
        for j in range(dim):
            if i != row or j != col:
                belief[i][j] = 1.0 * belief[i][j] / (P[board[i][j]] * belief[i][i] + 1.0 - belief[i][j])
                if belief[i][j] < sys.float_info.epsilon:
                    belief[i][j] = 0


def search(board, belief, target_row, target_col, dim, row, col):
    P = [0.1, 0.3, 0.7, 0.9] # P(Target not found in Cell[i]| Target is in Cell[i]), probability for flat, hill, forest, cave
    if target_row == row and target_col == col:
        if is_found(P[board[row][col]]) == False:
            update(board, belief, dim, row, col)
        else:
            return True
    else:
        update(board, belief, dim, row, col)
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
        flag = search(board, belief, target_row, target_col, board_dim, s_row, s_col)
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
    print "belief_rule2 :"
    print belief_rule2
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
        flag = search(board, belief, target_row, target_col, board_dim, s_row, s_col)
        belief_rule2 = rule2_belief(board, belief, board_dim)
        print "belief_rule2 :"
        print belief_rule2
        print "belief: "
        print belief
        if flag == True:
            break
    print "max step"
    return step


def find_min_cost(cost):
    min = float("inf")
    for i in range(len(cost)):
        for j in range(len(cost)):
            if(cost[i][j] < min):
                min = cost[i][j]
                row = i
                col = j
    min_cost_point = [row, col]
    return min_cost_point


def cost_mat(belief_rule2,current_point):
    cost = np.zeros((len(belief_rule2), len(belief_rule2)))
    for i in range(0, len(belief_rule2)):
        for j in range(0, len(belief_rule2)):
            if belief_rule2[i][j] == 0:
                cost[i][j] = float("inf")
            elif belief_rule2[i][j] != 0:
                cost[i][j] = (abs(i - current_point[0]) + abs(j - current_point[1]) + 1)*(1 / abs(belief_rule2[i][j]))
           # cost[i][j] = abs(i - current_point[0]) + abs(j - current_point[1]) + 1 + 2 / belief_rule2[i][j]
    return cost


def actual_cost(current_point, next_point):
    actual_cost = abs(current_point[0] - next_point[0]) + abs(current_point[1] - next_point[1]) + 1
    return actual_cost


def cost_rule3_solver(board_dim,begin_point):
    board, belief, target_row, target_col = random_board(board_dim)
    print "board: "
    print board
    print "target position: "
    print target_row, target_col
    print "belief: "
    print belief
    belief_rule2 = rule2_belief(board, belief, board_dim)
    # P(Target not found in Cell[i]| Target is in Cell[i]), probability for flat, hill, forest, cave
    cost = cost_mat(belief_rule2,begin_point)
    total_cost = 0
    current_point = begin_point
    while True:
        next_point = find_min_cost(cost)
        total_cost += actual_cost(current_point, next_point)
        current_point = next_point
        s_row, s_col = current_point[0], current_point[1]
        print "min cost point"
        print s_row, s_col
        flag = search(board, belief, target_row, target_col, board_dim, s_row, s_col)
        belief_rule2 = rule2_belief(board, belief, board_dim)
        cost = cost_mat(belief_rule2,current_point)
        if flag == True:
            break
        if total_cost > 1000000:
            total_cost = None
            break
    print "Total cost"
    return total_cost


def cost_rule2_solver(board_dim,begin_point):
    board, belief, target_row, target_col = random_board(board_dim)
    print "board: "
    print board
    print "target position: "
    print target_row, target_col
    print "belief: "
    print belief
    belief_rule2 = rule2_belief(board, belief, board_dim)
    # P(Target not found in Cell[i]| Target is in Cell[i]), probability for flat, hill, forest, cave
    # cost = cost_mat(belief_rule2,begin_point)
    total_cost = 0
    current_point = begin_point
    while True:
        row, col = find_max_prob(belief_rule2, board_dim)
        next_point = row, col
        total_cost += actual_cost(current_point, next_point)
        current_point = next_point
        s_row, s_col = current_point[0], current_point[1]
        print "min cost point"
        print s_row, s_col
        flag = search(board, belief, target_row, target_col, board_dim, s_row, s_col)
        belief_rule2 = rule2_belief(board, belief, board_dim)
        # cost = cost_mat(belief_rule2,current_point)
        if flag == True:
            break
        if total_cost > 1000000:
            total_cost = None
            break
    print "Total cost"
    return total_cost


def cost_rule1_solver(board_dim,begin_point):
    board, belief, target_row, target_col = random_board(board_dim)
    print "board: "
    print board
    print "target position: "
    print target_row, target_col
    print "belief: "
    print belief
    belief_rule2 = rule2_belief(board, belief, board_dim)
    # P(Target not found in Cell[i]| Target is in Cell[i]), probability for flat, hill, forest, cave
    cost = cost_mat(belief_rule2,begin_point)
    total_cost = 0
    current_point = begin_point
    while True:
        row, col = find_max_prob(belief, board_dim)
        next_point = row, col
        total_cost += actual_cost(current_point, next_point)
        current_point = next_point
        s_row, s_col = current_point[0], current_point[1]
        print "min cost point"
        print s_row, s_col
        flag = search(board, belief, target_row, target_col, board_dim, s_row, s_col)
        # belief_rule2 = rule2_belief(board, belief, board_dim)
        # cost = cost_mat(belief_rule2,current_point)
        if flag == True:
            break
        if total_cost > 1000000:
            total_cost = None
            break
    print "Total cost"
    return total_cost

def movingtarget(current_target,dim):
    moving_number = random.randrange(0, 4)
    if moving_number == 1:    # case 1: up
        row = current_target[0] - 1
        col = current_target[1]
        if row < 0:
            print "row jjj"
            row, col = movingtarget(current_target, dim)

    elif moving_number == 2:  # case 2: down
        row = current_target[0] + 1
        col = current_target[1]
        if row > 49:
            row, col = movingtarget(current_target, dim)

    elif moving_number == 3:  # case 3: left
        row = current_target[0]
        col = current_target[1] - 1
        if col < 0:
            print "col jin"
            row, col = movingtarget(current_target, dim)

    else:                     # case 4: right
        row = current_target[0]
        col = current_target[1] + 1
        if col > 49:
            row, col = movingtarget(current_target, dim)

    next_target = row, col
    return next_target

def surveillance(board, current_target, next_target):
    print board[current_target[0]][current_target[1]], board[next_target[0]][next_target[1]]
    return board[current_target[0]][current_target[1]], board[next_target[0]][next_target[1]]

def judge_Fisrt(TypeList1, TypeList2):
    if(TypeList1[0] == TypeList2[0]):
        predit_next_target_type = TypeList2[1]
    if (TypeList1[0] == TypeList2[1]):
        predit_next_target_type = TypeList2[0]

    if (TypeList1[1] == TypeList2[0]):
        predit_next_target_type = TypeList2[1]
    if (TypeList1[1] == TypeList2[1]):
        predit_next_target_type = TypeList2[0]

    if ((TypeList1[0] == TypeList1[1]) and (TypeList1[1] == TypeList2[0]) and (TypeList2[0] == TypeList2[1])):
        predit_next_target_type = -1
    print predit_next_target_type
    return predit_next_target_type

def judge_Second(TypeList, last_target_type):
    if(last_target_type == TypeList[0]):
        predit_next_target_type = TypeList[1]
    if(last_target_type == TypeList[1]):
        predit_next_target_type = TypeList[0]
    return predit_next_target_type

def find_type_max_prob(board, belief, dim, predit_next_type, TypeList):
    max = -1
    col = 0
    row = 0
    if (predit_next_type != -1):
        for i in range(dim):
            for j in range(dim):
                if (belief[i][j] > max and board[i][j] == predit_next_type):
                    max = belief[i][j]
                    col = i
                    row = j
        return col, row
    else:
        for i in range(dim):
            for j in range(dim):
                if (belief[i][j] > max and board[i][j] == TypeList[0]):
                    if (board[i - 1][j] == TypeList[0]):
                        max = belief[i][j]
                        col = i - 1
                        row = j
                    if (board[i + 1][j] == TypeList[0]):
                        max = belief[i][j]
                        col = i + 1
                        row = j
                    if (board[i][j - 1] == TypeList[0]):
                        max = belief[i][j - 1]
                        col = i
                        row = j - 1
                    if (board[i][j + 1] == TypeList[0]):
                        max = belief[i][j]
                        col = i
                        row = j + 1
        return col, row


def moving_rule1_solver(board_dim):
    board, belief, target_row, target_col = random_board(board_dim)
    # print "board: "
    # print board
    # print "target position: "
    # print target_row, target_col
    # print "belief: "
    # print belief
    print '_________________'
    s_row, s_col = find_max_prob(belief, board_dim)  # step1: search the max prob point
    search(board, belief, target_row, target_col, board_dim, s_row, s_col)
    current_target = target_row, target_col
    next_target = movingtarget(current_target, board_dim)
    print current_target, next_target
    TypeList1 = surveillance(board, current_target, next_target)
    s_row, s_col = find_max_prob(belief, board_dim)  # step2: search the max prob point
    search(board, belief, target_row, target_col, board_dim, s_row, s_col)
    current_target = next_target
    next_target = movingtarget(current_target, board_dim)
    print current_target, next_target
    TypeList2 = surveillance(board, current_target, next_target)
    predit_next_target_type = judge_Fisrt(TypeList1, TypeList2)

    step = 2
    while True:
        step += 1
        s_row, s_col = find_type_max_prob(board, belief, board_dim, predit_next_target_type, TypeList2)
        print "type max prob point"
        print s_row, s_col
        print "------"
        flag = search(board, belief, target_row, target_col, board_dim, s_row, s_col)
        current_target = next_target
        next_target = movingtarget(current_target, board_dim)
        if predit_next_target_type == -1:
            Last_target_type = TypeList2[0]
        else:
            Last_target_type = predit_next_target_type
        TypeList2 = surveillance(board, current_target, next_target)
        predit_next_target_type = judge_Second(TypeList2, Last_target_type)
        print "belief: "
        print belief
        if flag == True:
            break
    print "max step"
    return step

def moving_rule2_solver(board_dim):
    board, belief, target_row, target_col = random_board(board_dim)
    # print "board: "
    # print board
    # print "target position: "
    # print target_row, target_col
    # print "belief: "
    # print belief
    print '_________________'
    belief_rule2 = rule2_belief(board, belief, board_dim)
    s_row, s_col = find_max_prob(belief_rule2, board_dim)  # step1: search the max prob point
    search(board, belief, target_row, target_col, board_dim, s_row, s_col)
    current_target = target_row, target_col
    next_target = movingtarget(current_target, board_dim)
    print current_target, next_target
    TypeList1 = surveillance(board, current_target, next_target)

    belief_rule2 = rule2_belief(board, belief, board_dim)  # step2: search the max prob point
    s_row, s_col = find_max_prob(belief_rule2, board_dim)
    search(board, belief, target_row, target_col, board_dim, s_row, s_col)
    current_target = next_target
    next_target = movingtarget(current_target, board_dim)
    print current_target, next_target
    TypeList2 = surveillance(board, current_target, next_target)
    predit_next_target_type = judge_Fisrt(TypeList1, TypeList2)

    step = 2
    while True:
        step += 1
        belief_rule2 = rule2_belief(board, belief, board_dim)
        s_row, s_col = find_type_max_prob(board, belief_rule2, board_dim, predit_next_target_type, TypeList2)
        print "type max prob point"
        print s_row, s_col
        print "------"
        flag = search(board, belief, target_row, target_col, board_dim, s_row, s_col)
        current_target = next_target
        next_target = movingtarget(current_target, board_dim)
        if predit_next_target_type == -1:
            Last_target_type = TypeList2[0]
        else:
            Last_target_type = predit_next_target_type
        TypeList2 = surveillance(board, current_target, next_target)
        predit_next_target_type = judge_Second(TypeList2, Last_target_type)
        print "belief: "
        print belief
        if flag == True:
            break
    print "max step"
    return step
def __main():
    # board_dim = int(input("Please enter a number indicating the dimension of grid: "))
    board_dim = 50
    begin_point = [0, 0]
    # cell_prob = float(input("Please enter a float number indicating the probability of flat terrain: "))
    # print rule2_solver(board_dim)
    # print cost_rule1_solver(board_dim,begin_point)
    print moving_rule1_solver(board_dim)


__main()
# next_point = movingtarget([1, 2])
# print next_point
