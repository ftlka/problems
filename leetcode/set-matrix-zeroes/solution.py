def mark_future_zeros(matrix, r_idx, c_idx):
	next_start = []

	# for row
	for i in range(len(matrix[0])):
		if i != c_idx and matrix[r_idx][i] == 0 and not next_start:
			next_start = [r_idx, c_idx]
		elif matrix[r_idx][i] != 0 or i == c_idx:
			# making sure to leave all zeroes except for current one
			matrix[r_idx][i] = 'x'

	# for column
	for i in range(len(matrix)):
		if matrix[i][c_idx] != 0:
			# making sure to leave all zeroes (without or i == r_idx, bc we already did it)
			matrix[i][c_idx] = 'x'

	if not next_start:
		next_start = [-1, -1]
	
	return next_start


def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Im finding all the zeros and creating rows and columns of xs
        r_idx = 0
        while r_idx < len(matrix):
        	c_idx = 0
        	while c_idx < len(matrix[0]):
        		if matrix[r_idx][c_idx] == 0:
        			next_start = mark_future_zeros(matrix, r_idx, c_idx)
        			if next_start != [-1, -1]:
        				r_idx, c_idx = next_start
        			else:
        				c_idx += 1
        		else:		
        			c_idx += 1
        	r_idx += 1

        # Now we replace xs with 0s
        for r_idx in range(len(matrix)):
        	for c_idx in range(len(matrix[0])):
        		if matrix[r_idx][c_idx] == 'x':
        			matrix[r_idx][c_idx] = 0
