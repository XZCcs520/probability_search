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


elapsed = (time.clock() - start)
print("Time used:", elapsed)