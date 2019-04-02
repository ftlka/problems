from solution import spiralOrder


matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
assert spiralOrder(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12]
]
assert spiralOrder(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


assert spiralOrder([[]]) == []


assert spiralOrder([]) == []


matrix = [
	[1, 2],
	[3, 4],
	[5, 6],
	[7, 8]
]
assert spiralOrder(matrix) == [1, 2, 4, 6, 8, 7, 5, 3]
