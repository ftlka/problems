from solution import canCompleteCircuit

#basic tests
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
assert canCompleteCircuit(gas, cost) == 3

gas  = [2, 3, 4]
cost = [3, 4, 3]
assert canCompleteCircuit(gas, cost) == -1

#local minimum
gas = [1, 1, 3, 1, 100]
cost = [1, 1, 1, 6, 1]
assert canCompleteCircuit(gas, cost) == 4
