class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue

                if board[row][col] in rows[row]:
                    return False
                if board[row][col] in cols[col]:
                    return False
                if board[row][col] in grid[row // 3][col // 3]:
                    return False

                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                grid[row // 3][col // 3].add(board[row][col])

        return True
