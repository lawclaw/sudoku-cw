# Brute force solver
# TODO: Bruteforce solver

def find_empty_square(current_board):
    for r in range(9):
        for c in range(9):
            if current_board[r][c] == 0:
                return r, c

    return None, None


def is_valid(board, guess, row, col):
    # Rule 1: No duplicates in same row
    if guess in board[row]:
        return False

    # Rule 2: No duplicates in same column
    for i in range(9):
        if board[i][col] == guess:
            return False

    # Rule 3: No duplicates in 3x3 grids
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if board[r][c] == guess:
                return False

    return True


def brute_solve(board):
    row, col = find_empty_square(board)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(board, guess, row, col):
            board[row][col] = guess

            if brute_solve(board):
                return True

        board[row][col] = 0

    return False
