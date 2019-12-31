class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        rows, cols = len(matrix), len(matrix[0])
        x, y = rows - 1, 0

        while x >= 0 and y < cols:
            if matrix[x][y] > target:
                x -= 1
            elif matrix[x][y] < target:
                y += 1
            else:
                return True

        return False
