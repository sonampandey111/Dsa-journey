class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]

        def solve(row, cols, diag1, diag2):
            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                solve(row + 1, cols, diag1, diag2)

                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        solve(0, set(), set(), set())
        return ans

        

        