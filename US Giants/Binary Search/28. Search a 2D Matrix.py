class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if matrix is None or len(matrix) == 0:
            return False

        # m: row; n: col
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows * cols - 1
        while left + 1 < right:
            mid = left + (right - left) // 2

            x, y = mid // cols, mid % cols

            if matrix[x][y] > target:
                right = mid
            else:
                left = mid

        x, y = left // cols, left % cols
        if matrix[x][y] == target:
            return True

        x, y = right // cols, right % cols
        if matrix[x][y] == target:
            return True

        return False
