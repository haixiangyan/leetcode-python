class Solution:
    def __init__(self):
        self.direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board, word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if self.dfs(board, i, j, rows, cols, word, visited):
                    return True

        return False

    def dfs(self, board, x, y, rows, cols, word, visited):
        if word == '':
            return True

        if not (0 <= x < rows and 0 <= y < cols):
            return False

        if board[x][y] == word[0] and not visited[x][y]:
            visited[x][y] = True

            for delta_x, delta_y in self.direction:
                if self.dfs(board, x + delta_x, y + delta_y, rows, cols, word[1:], visited):
                    return True

            visited[x][y] = False

        return False
