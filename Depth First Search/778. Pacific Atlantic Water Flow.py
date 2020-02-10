class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
    """
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return []

        pacific, atlantic = set(), set()
        rows, cols = len(matrix), len(matrix[0])

        # Up & Bottom
        for i in range(cols):
            self.dfs(0, i, matrix, pacific, 0, rows, cols)
            self.dfs(rows - 1, i, matrix, atlantic, 0, rows, cols)

        # Left & Right
        for i in range(rows):
            self.dfs(i, 0, matrix, pacific, 0, rows, cols)
            self.dfs(i, cols - 1, matrix, atlantic, 0, rows, cols)

        return list(pacific & atlantic)

    def dfs(self, x, y, matrix, visited, height, rows, cols):
        if not (0 <= x < rows and 0 <= y < cols) or (x, y) in visited:
            return

        if matrix[x][y] < height:
            return

        visited.add((x, y))

        for delta in range(4):
            self.dfs(x + self.dx[delta], y + self.dy[delta], matrix, visited, matrix[x][y], rows, cols)
