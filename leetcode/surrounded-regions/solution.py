from collections import deque, namedtuple


def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """
    if not board:
    	return

    coord = namedtuple('coord', ['row', 'col'])
    queue = deque()

    first_row, last_row = board[0], board[-1]
    first_col, last_col = [row[0] for row in board], [row[-1] for row in board]

    for i, el in enumerate(first_row):
        if el == 'O':
            board[0][i] = '!'
            queue.appendleft(coord(0, i))
    for i, el in enumerate(last_row):
        if el == 'O':
            board[len(board) - 1][i] = '!'
            queue.appendleft(coord(len(board) - 1, i))
    for i, el in enumerate(first_col):
        if el == 'O':
            board[i][0] = '!'
            queue.appendleft(coord(i, 0))
    for i, el in enumerate(last_col):
        if el == 'O':
            board[i][len(board[0]) - 1] = '!'
            queue.appendleft(coord(i, len(board[0]) - 1))

    while queue:
        cur_row, cur_col = queue.pop()
        # if we can move up
        if cur_row > 0 and board[cur_row - 1][cur_col] == 'O':
            board[cur_row - 1][cur_col] = '!'
            queue.appendleft(coord(cur_row - 1, cur_col))
        # if we can move down
        if cur_row < len(board) - 1 and board[cur_row + 1][cur_col] == 'O':
            board[cur_row + 1][cur_col] = '!'
            queue.appendleft(coord(cur_row + 1, cur_col))
        # if we can move left
        if cur_col > 0 and board[cur_row][cur_col - 1] == 'O':
            board[cur_row][cur_col - 1] = '!'
            queue.appendleft(coord(cur_row, cur_col - 1))
        # if we can move right
        if cur_col < len(board[0]) - 1 and board[cur_row][cur_col + 1] == 'O':
            board[cur_row][cur_col + 1] = '!'
            queue.appendleft(coord(cur_row, cur_col + 1))

    for row_idx in range(len(board)):
        for col_idx in range(len(board[0])):
            if board[row_idx][col_idx] == 'O':
                board[row_idx][col_idx] = 'X'
            elif board[row_idx][col_idx] == '!':
                board[row_idx][col_idx] = 'O'
