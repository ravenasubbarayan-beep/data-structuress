def nqueens(n):
    solutions = []

    def backtrack(row, columns, diagonals1, diagonals2, board):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            d1 = row - col
            d2 = row + col

            if col not in columns and d1 not in diagonals1 and d2 not in diagonals2:
                board.append(col)
                columns.add(col)
                diagonals1.add(d1)
                diagonals2.add(d2)

                backtrack(row + 1, columns, diagonals1, diagonals2, board)

                board.pop()
                columns.remove(col)
                diagonals1.remove(d1)
                diagonals2.remove(d2)

    backtrack(0, set(), set(), set(), [])

    for sol in solutions:
        for col in sol:
            print(" ".join("Q" if j == col else "." for j in range(n)))
        print()

nqueens(4)