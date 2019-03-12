from solution import coinChange


assert coinChange([1, 2, 5], 11) == 3

assert coinChange([2], 3) == -1

assert coinChange([1], 2) == 2

assert coinChange([1], 0) == 0

assert coinChange([2], 1) == -1

assert coinChange([2, 5, 10, 1], 27) == 4
