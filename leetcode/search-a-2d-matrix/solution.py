from collections import namedtuple


def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    coord = namedtuple('Coordinate', ['row', 'col'])
    lo, hi = coord(0, 0), coord(len(matrix)-1, len(matrix[0])-1)
    
    if target < matrix[lo.row][lo.col] or target > matrix[hi.row][hi.col]:
        return False

    while lo.row <= hi.row and lo.col <= hi.col:
        if lo.row == hi.row and lo.col == hi.col and matrix[lo.row][lo.col] != target:
            return False

        if lo.row != hi.row:
            mid = coord((hi.row + lo.row) // 2, hi.col)
        else:
            mid = coord(lo.row, (hi.col + lo.col) // 2)
        mid_val = matrix[mid.row][mid.col]

        if target == mid_val:
            return True
        elif target < mid_val:
            hi = mid
        else:
            if mid.row != hi.row:
                lo = coord(mid.row + 1, 0)
            else:
                lo = coord(mid.row, mid.col + 1)


    return False
