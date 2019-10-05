class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return 0

        occurance = 0
        rows, cols = len(matrix), len(matrix[0])
        x, y = rows - 1, 0

        while x >= 0 and y < cols:
            if matrix[x][y] < target:
                y += 1
            elif matrix[x][y] > target:
                x -= 1
            else:
                x -= 1
                y += 1
                occurance += 1

        return occurance
