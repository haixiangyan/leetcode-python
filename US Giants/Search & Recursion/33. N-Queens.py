class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        results = []

        self.search(n, [], results)

        return results

    def search(self, n, rows, results):
        row = len(rows)

        if row == n:
            results.append(self.draw_chessboard(rows))
            return

        for col in range(n):
            if not self.is_valid(rows, row, col):
                continue

            rows.append(col)
            self.search(n, rows, results)
            rows.pop()

    def draw_chessboard(self, rows):
        n = len(rows)
        board = []
        for i in range(n):
            row = ['Q' if j == rows[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board

    def is_valid(self, rows, row, col):
        for r, c in enumerate(rows):
            if c == col:
                return False
            if r - c == row - col or r + c == row + col:
                return False
        return True
