class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        rows, cols = len(matrix), len(matrix[0])

        x, y = rows - 1, 0
        count = 0
        while x >= 0 and y < cols:
            if matrix[x][y] < target:
                # Shift right
                y += 1
            elif matrix[x][y] > target:
                # Shift top
                x -= 1
            else:
                x -= 1
                y += 1
                count += 1

        return count
