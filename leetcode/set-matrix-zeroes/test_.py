from solution import setZeroes


# test 1
original_matrix = [
	[1,1,1],
	[1,0,1],
	[1,1,1]
]

expected_matrix = [
	[1,0,1],
	[0,0,0],
	[1,0,1]
]

setZeroes(original_matrix)

assert original_matrix == expected_matrix


# test 2
original_matrix = [
	[0, 1, 2, 0],
	[3, 4, 5, 2],
	[1, 3, 1, 5]
]

expected_matrix = [
	[0, 0, 0, 0],
	[0, 4, 5, 0],
	[0, 3, 1, 0]
]

setZeroes(original_matrix)

assert original_matrix == expected_matrix
