class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        if len(board) == 0:
            return False
        if len(board[0]) == 0:
            return False

        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if self.dfs(board, word, visited, i, j):
                    return True

        return False

    def dfs(self, board, word, visited, x, y):
        rows, cols = len(board), len(board[0])
        # Check string boundary
        if word == '':
            return True
        # Check board boundary
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return False
        # Check visited
        if board[x][y] == word[0] and not visited[x][y]:
            visited[x][y] = True
            if self.dfs(board, word[1:], visited, x + 1, y) or self.dfs(board, word[1:], visited, x - 1, y) or self.dfs(board, word[1:], visited, x, y - 1) or self.dfs(board, word[1:], visited, x, y + 1):
                return True
            else:
                visited[x][y] = False

        return False
