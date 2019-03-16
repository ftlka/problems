from solution import countBits


# 0 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 100000
# 0 1 1  2  1   2   2   3   1    2    2    3    2    3    3    4    1
# 0 1 2  3  4   5   6   7   8    9    10   11   12   13   14   15   16

assert countBits(2) == [0, 1, 1]

assert countBits(5) == [0, 1, 1, 2, 1, 2]

assert countBits(10) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]

assert countBits(0) == [0]

assert countBits(1) == [0, 1]
