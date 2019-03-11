from solution import search

# basic tests
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
assert search(nums, target) == 4

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
assert search(nums, target) == -1

# empty list
assert search([], 3) == -1

# list with one element in nums
assert search([1], 1) == 0

# # list with one element not in nums
assert search([1], 2) == -1

assert search([3, 1], 0) == -1

assert search([1, 3], 1) == 0

assert search([5, 1, 3], 1) == 1

assert search([5, 1, 3], 3) == 2

assert search([1, 3, 5], 5) == 2

assert search([4, 5, 6, 7, 8, 1, 2, 3], 8) == 4
