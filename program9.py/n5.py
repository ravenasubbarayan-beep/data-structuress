def solve_nqueens(n):
    board = [-1] * n
    count = 0

    def is_safe(row, col):
        for prev in range(row):
            if board[prev] == col:
                return False
            if abs(board[prev] - col) == abs(prev - row):
                return False
        return True

    def backtrack(row):
        nonlocal count

        if row == n:
            count += 1
            print("\nSolution", count)

            for r in range(n):
                print(" ".join(
                    "Q" if board[r] == c else "."
                    for c in range(n)
                ))
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)

    if count == 0:
        print("No solution exists.")

    print("\nTotal Solutions:", count)


n = int(input("Enter the value of N: "))
solve_nqueens(n)