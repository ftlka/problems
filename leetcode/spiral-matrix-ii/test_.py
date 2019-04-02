from solution import generateMatrix


matrix = [
	[1, 2, 3],
	[8, 9, 4],
	[7, 6, 5]
]
assert generateMatrix(3) == matrix


assert generateMatrix(1) == [[1]]


matrix = [
	[1, 2],
	[4, 3]
]
assert generateMatrix(2) == matrix


matrix = [
	[1, 2, 3, 4],
	[12, 13, 14, 5],
	[11, 16, 15, 6],
	[10, 9, 8, 7]
]
assert generateMatrix(4) == matrix
