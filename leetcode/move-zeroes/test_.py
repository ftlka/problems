from solution import moveZeroes


assert moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]

assert moveZeroes([]) == []

assert moveZeroes([0, 0]) == [0, 0]

assert moveZeroes([1, 2]) == [1, 2]

assert moveZeroes([0, 0, 0, 1, 2, 3]) == [1, 2, 3, 0, 0, 0]
