def solve_nqueens(n):
    board = [-1] * n
    count = 0

    def safe(row, col):
        for i in range(row):
            if board[i] == col:
                return False
            if abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row):
        nonlocal count

        if row == n:
            count += 1
            print("Solution", count)

            for i in range(n):
                print(" ".join("Q" if board[i] == j else "." for j in range(n)))
            print()
            return

        for col in range(n):
            if safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    print("Total Solutions:", count)

solve_nqueens(4)