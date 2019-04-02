def get_num(n):
    for num in range(1, n ** 2 + 1):
        yield num


def generateMatrix(n):
    matrix = [[0] * n for i in range(n)]
    generator = get_num(n)

    left_bound, right_bound = 0, n - 1
    upper_bound, lower_bound = 0, n - 1
    row, col = 0, 0

    while True:
        # right
        if not col <= right_bound:
            break
        while col <= right_bound:
            matrix[row][col] = next(generator)
            col += 1
        col -= 1
        row += 1
        upper_bound += 1

        # down
        if not row <= lower_bound:
            break
        while row <= lower_bound:
            matrix[row][col] = next(generator)
            row += 1
        row -= 1
        col -= 1
        right_bound -= 1

        # left
        if not col >= left_bound:
            break
        while col >= left_bound:
            matrix[row][col] = next(generator)
            col -= 1
        col += 1
        row -= 1
        lower_bound -= 1

        # up
        if not row >= upper_bound:
            break
        while row >= upper_bound:
            matrix[row][col] = next(generator)
            row -= 1
        row += 1
        col += 1
        left_bound += 1

    return matrix
