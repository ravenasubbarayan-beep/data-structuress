def solve_nqueens(n):
    board = [-1] * n
    solutions = []

    def safe(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            if safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)

    for solution in solutions:
        for row in solution:
            print("." * row + "Q" + "." * (n - row - 1))
        print()

n = 4
solve_nqueens(n)