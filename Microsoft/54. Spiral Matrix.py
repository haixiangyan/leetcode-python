class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        up, down = 0, rows - 1
        left, right = 0, cols - 1
        order = []

        direction = 0

        while True:
            if direction == 0:
                for i in range(left, right + 1):
                    order.append(matrix[up][i])
                up += 1
            if direction == 1:
                for i in range(up, down + 1):
                    order.append(matrix[i][right])
                right -= 1
            if direction == 2:
                for i in range(right, left - 1, -1):
                    order.append(matrix[down][i])
                down -= 1
            if direction == 3:
                for i in range(down, up - 1, -1):
                    order.append(matrix[i][left])
                left += 1

            if left > right or up > down:
                break
            direction = (direction + 1) % 4

        return order
