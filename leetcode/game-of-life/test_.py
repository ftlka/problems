from solution import gameOfLife


board = [
	[0, 1, 0],
	[0, 0, 1],
	[1, 1, 1],
	[0, 0, 0]
]

expected_board = [
	[0, 0, 0],
	[1, 0, 1],
	[0, 1, 1],
	[0, 1, 0]
]

gameOfLife(board)

assert board == expected_board
