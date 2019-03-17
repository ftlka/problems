from solution import searchMatrix


matrix = [
	[1, 3, 5, 7],
  	[10, 11, 16, 20],
  	[23, 30, 34, 50]
]

assert searchMatrix(matrix, 1)

assert searchMatrix(matrix, 3)

assert searchMatrix(matrix, 7)

assert searchMatrix(matrix, 10)

assert searchMatrix(matrix, 20)

assert searchMatrix(matrix, 50)

assert not searchMatrix(matrix, 13)

assert not searchMatrix(matrix, -1)

assert not searchMatrix(matrix, 52)

assert not searchMatrix(matrix, 2)

assert not searchMatrix(matrix, 8)
