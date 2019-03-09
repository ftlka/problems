from solution import nextPermutation

#basic tests
l = [1, 2, 3]
nextPermutation(l)
assert l == [1, 3, 2]

nextPermutation(l)
assert l == [2, 1, 3]

nextPermutation(l)
assert l == [2, 3, 1]

nextPermutation(l)
assert l == [3, 1, 2]

nextPermutation(l)
assert l == [3, 2, 1]

nextPermutation(l)
assert l == [1, 2, 3]

# with repetations
l = [1, 2, 2]
nextPermutation(l)
assert l == [2, 1, 2]

# and just more complex
l = [7, 6, 4, 5, 9, 8, 1]
nextPermutation(l)
assert l == [7, 6, 4, 8, 1, 5, 9]