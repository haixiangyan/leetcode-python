class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        if not matrix:
            return matrix

        rows, cols = len(matrix), len(matrix[0])
        up, down, left, right = 0, rows - 1, 0, cols - 1
        direct = 0
        order = []

        while True:
            if direct == 0:
                for i in range(left, right + 1):
                    order.append(matrix[up][i])
                up += 1
            if direct == 1:
                for i in range(up, down + 1):
                    order.append(matrix[i][right])
                right -= 1
            if direct == 2:
                for i in range(right, left - 1, -1):
                    order.append(matrix[down][i])
                down -= 1
            if direct == 3:
                for i in range(down, up - 1, -1):
                    order.append(matrix[i][left])
                left += 1

            if left > right or up > down:
                break
            direct = (direct + 1) % 4

        return order
