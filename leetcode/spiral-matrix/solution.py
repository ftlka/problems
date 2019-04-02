def spiralOrder(matrix):
    if not matrix:
        return []
    res = []
    left_bound, right_bound = 0, len(matrix[0]) - 1
    upper_bound, lower_bound = 0, len(matrix) - 1
    row, col = 0, 0

    while True:
        # go right
        if col <= right_bound:
            while col <= right_bound:
                res.append(matrix[row][col])
                col += 1
            upper_bound += 1
            col -= 1
            row += 1
        else:
            break

        # go down
        if row <= lower_bound:
            while row <= lower_bound:
                res.append(matrix[row][col])
                row += 1
            right_bound -= 1
            row -= 1
            col -= 1
        else:
            break

        # go left
        if col >= left_bound:
            while col >= left_bound:
                res.append(matrix[row][col])
                col -= 1
            lower_bound -= 1
            col += 1
            row -= 1
        else:
            break

        # go up
        if row >= upper_bound:
            while row >= upper_bound:
                res.append(matrix[row][col])
                row -= 1
            left_bound += 1
            row += 1
            col += 1
        else:
            break

    return res
