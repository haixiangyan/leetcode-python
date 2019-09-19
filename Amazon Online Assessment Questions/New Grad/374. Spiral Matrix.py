class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        if not matrix:
            return None

        rows, cols = len(matrix), len(matrix[0])
        up, down = 0, rows - 1
        left, right = 0, cols - 1

        results = []
        direct = 0

        while True:
            # 向右
            if direct == 0:
                for i in range(left, right + 1):
                    results.append(matrix[up][i])
                up += 1
            # 向下
            if direct == 1:
                for i in range(up, down + 1):
                    results.append(matrix[i][right])
                right -= 1
            # 向左
            if direct == 2:
                for i in range(right, left - 1, -1):
                    results.append(matrix[down][i])
                down -= 1
            # 向上
            if direct == 3:
                for i in range(down, up - 1, -1):
                    results.append(matrix[i][left])
                left += 1

            if left > right or up > down:
                return results

            direct = (direct + 1) % 4
