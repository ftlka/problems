def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    """
    for r_idx in range(len(board)):
        for c_idx in range(len(board[0])):
            alive_neighbours = 0

            can_go_up = r_idx > 0
            can_go_left = c_idx > 0
            can_go_down = r_idx < len(board) - 1
            can_go_right = c_idx < len(board[0]) - 1

            # diag left
            if can_go_up and can_go_left and board[r_idx-1][c_idx-1] in [1, 'd']:
                alive_neighbours += 1
            # straight up
            if can_go_up and board[r_idx-1][c_idx] in [1, 'd']:
                alive_neighbours += 1
            # diag right
            if can_go_up and can_go_right and board[r_idx-1][c_idx+1] in [1, 'd']:
                alive_neighbours += 1

            # left
            if can_go_left and board[r_idx][c_idx-1] in [1, 'd']:
                alive_neighbours += 1
            # right
            if can_go_right and board[r_idx][c_idx+1] in [1, 'd']:
                alive_neighbours += 1

            # diag left
            if can_go_down and can_go_left and board[r_idx+1][c_idx-1] in [1, 'd']:
                alive_neighbours += 1
            # straight down
            if can_go_down and board[r_idx+1][c_idx] in [1, 'd']:
                alive_neighbours += 1
            # diag right
            if can_go_down and can_go_right and board[r_idx+1][c_idx+1] in [1, 'd']:
                alive_neighbours += 1

            # and now we have 4 cases:
            # 0 -> 0 - do nothing
            # 0 -> 1 - change to 'r' for resurrect
            # 1 -> 0 - change to 'd' for death
            # 1 -> 1 - do nothing
            if board[r_idx][c_idx] == 0:
                if alive_neighbours == 3:
                    board[r_idx][c_idx] = 'r'
            else:
                if alive_neighbours > 3 or alive_neighbours < 2:
                    board[r_idx][c_idx] = 'd'

    # update the board
    for r_idx in range(len(board)):
        for c_idx in range(len(board[0])):
            if board[r_idx][c_idx] == 'r':
                board[r_idx][c_idx] = 1
            if board[r_idx][c_idx] == 'd':
                board[r_idx][c_idx] = 0
