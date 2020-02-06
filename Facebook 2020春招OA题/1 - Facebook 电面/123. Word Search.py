class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
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

        if x < 0 or x >= rows or y < 0 or y >= cols:
            return False

        if board[x][y] == word[0] and not visited[x][y]:
            visited[x][y] = True

            for delta in range(4):
                if self.dfs(board, x + self.dx[delta], y + self.dy[delta], rows, cols, word[1:], visited):
                    return True

            visited[x][y] = False

        return False
