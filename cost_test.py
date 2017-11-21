import bayesian
import numpy as np
import time

start = time.clock()




board_dim = 50
begin_point = [0,0]
k = 10
cost_rule3 = []
cost_rule2 = []
cost_rule1 = []

for i in range (0, k):
    print "STEP:\n________________"
    print i
    cost_rule3.append(bayesian.cost_rule3_solver(board_dim,begin_point))
while None in cost_rule3:
    cost_rule3.remove(None)
mean_cost_rule3 = np.mean(np.array(cost_rule3))

# for i in range (0, k):
#     print "STEP:\n________________"
#     print i
#     cost_rule2.append(bayesian.cost_rule2_solver(board_dim,begin_point))
# while None in cost_rule2:
#     cost_rule2.remove(None)
# mean_cost_rule2 = np.mean(np.array(cost_rule2))
#
# for i in range (0, k):
#     print "STEP:\n________________"
#     print i
#     cost_rule1.append(bayesian.cost_rule1_solver(board_dim,begin_point))
# while None in cost_rule1:
#     cost_rule1.remove(None)
# mean_cost_rule1 = np.mean(np.array(cost_rule1))

print "cost rule3"
print cost_rule3
print "mean cost rule3"
print mean_cost_rule3

# print "cost rule2"
# print cost_rule2
# print "mean cost rule2"
# print mean_cost_rule2
#
# print "cost rule1"
# print cost_rule1
# print "mean cost rule1"
# print mean_cost_rule1

'''
def fixed_map test():
    #board_dim = 50
    #board, belief, target_row, target_col = bayesian.random_board(board_dim)

    # Caution: you must change bayesian.py a little to run fixed board iteration.

    avg = []
    sum = 0
    while True:
        board_dim = 50
        board, belief, target_row, target_col = bayesian.random_board(board_dim)
        if board[target_row][target_col] == 0:
            sum = 0
            for i in range(5):
                sum += bayesian.rule1_solver(board, belief, target_row, target_col)
            print "0-rule1"
            print sum/5
            avg.append(sum / 5)
            sum = 0
            for i in range(5):
                sum += bayesian.rule2_solver(board, belief, target_row, target_col)
            print "0-rule2"
            print sum/5
            avg.append(sum / 5)

            break

    while True:
        board_dim = 50
        board, belief, target_row, target_col = bayesian.random_board(board_dim)
        if board[target_row][target_col] == 1:
            sum = 0
            for i in range(5):
                sum += bayesian.rule1_solver(board, belief, target_row, target_col)
            print "1-rule1"
            print sum / 5
            avg.append(sum / 5)
            sum = 0
            for i in range(5):
                sum += bayesian.rule2_solver(board, belief, target_row, target_col)
            print "1-rule2"
            print sum / 5
            avg.append(sum / 5)

            break

    while True:
        board_dim = 50
        board, belief, target_row, target_col = bayesian.random_board(board_dim)
        if board[target_row][target_col] == 2:
            sum = 0
            for i in range(5):
                sum += bayesian.rule1_solver(board, belief, target_row, target_col)
            print sum / 5
            avg.append(sum / 5)
            sum = 0
            for i in range(5):
                sum += bayesian.rule2_solver(board, belief, target_row, target_col)
            print sum / 5
            avg.append(sum / 5)

            break

    while True:
        board_dim = 50
        board, belief, target_row, target_col = bayesian.random_board(board_dim)
        if board[target_row][target_col] == 3:
            sum = 0
            for i in range(5):
                sum += bayesian.rule1_solver(board, belief, target_row, target_col)
            print sum / 5
            avg.append(sum / 5)
            sum = 0
            for i in range(5):
                sum += bayesian.rule2_solver(board, belief, target_row, target_col)
            print sum / 5
            avg.append(sum / 5)

            break




    print "------------------------------------------"
    for i in avg:
        print i
'''
elapsed = (time.clock() - start)
print("Time used:", elapsed)
