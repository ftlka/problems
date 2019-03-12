from solution import lengthOfLIS


assert lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4

assert lengthOfLIS([0]) == 1

assert lengthOfLIS([1, 2]) == 2

assert lengthOfLIS([-2, -1]) == 2

#empty array
assert lengthOfLIS([]) == 0
