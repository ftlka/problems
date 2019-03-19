from solution import solve


# test 1
board = [
	['X', 'X', 'X', 'X'],
	['X', 'O', 'O', 'X'],
	['X', 'X', 'O', 'X'],
	['X', 'O', 'X', 'X'],
]

expected = [
	['X', 'X', 'X', 'X'],
	['X', 'X', 'X', 'X'],
	['X', 'X', 'X', 'X'],
	['X', 'O', 'X', 'X'],
]

solve(board)
assert board == expected


# test 2 - vertical neighbour lives
board = [
	['X', 'X', 'X', 'X'],
	['X', 'O', 'O', 'X'],
	['X', 'O', 'O', 'X'],
	['X', 'O', 'X', 'X'],
]

expected = [
	['X', 'X', 'X', 'X'],
	['X', 'O', 'O', 'X'],
	['X', 'O', 'O', 'X'],
	['X', 'O', 'X', 'X'],
]

solve(board)
assert board == expected


# test 3 - horizontal neighbour lives
board = [
	['X', 'X', 'X', 'X'],
	['O', 'O', 'O', 'X'],
	['X', 'O', 'O', 'X'],
	['X', 'X', 'X', 'X'],
]

expected = [
	['X', 'X', 'X', 'X'],
	['O', 'O', 'O', 'X'],
	['X', 'O', 'O', 'X'],
	['X', 'X', 'X', 'X'],
]

solve(board)
assert board == expected


# test 4 - everybody dies
board = [
	['X', 'X', 'X', 'X'],
	['X', 'O', 'O', 'X'],
	['X', 'O', 'O', 'X'],
	['X', 'X', 'X', 'X'],
]

expected = [
	['X', 'X', 'X', 'X'],
	['X', 'X', 'X', 'X'],
	['X', 'X', 'X', 'X'],
	['X', 'X', 'X', 'X'],
]

solve(board)
assert board == expected


# test 5
board = [
	['O', 'X', 'X', 'O', 'X'],
	['X', 'O', 'O', 'X', 'O'],
	['X', 'O', 'X', 'O', 'X'],
	['O', 'X', 'O', 'O', 'O'],
	['X', 'X', 'O', 'X', 'O'],
]

expected = [
	['O', 'X', 'X', 'O', 'X'],
	['X', 'X', 'X', 'X', 'O'],
	['X', 'X', 'X', 'O', 'X'],
	['O', 'X', 'O', 'O', 'O'],
	['X', 'X', 'O', 'X', 'O'],
]

solve(board)
assert board == expected


# test 6 - empty board
board = []
solve(board)
assert board == []


# test 7 - with 1 element
board = [['O']]
solve(board)
assert board == [['O']]
