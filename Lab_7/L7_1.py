n = int(input("Enter value of N: "))

board = [[0] * n for _ in range(n)]


def test(board, r, c):
    for i in range(n):
        if board[i][c] == 1:
            return False
        if board[r][i] == 1:
            return False
        if r - i >= 0 and c - i >= 0 and board[r - i][c - i] == 1:
            return False
        if r - i >= 0 and c + i < n and board[r - i][c + i] == 1:
            return False
    return True


def print_b(board):
    print("Final Board:")
    for l in board:
        print(l)
    quit()


def solve(board, r):
    if r == len(board):
        print_b(board)

    for c in range(n):
        if test(board, r, c):
            board[r][c] = 1
            solve(board, r + 1)
            board[r][c] = 0


solve(board, 0)
