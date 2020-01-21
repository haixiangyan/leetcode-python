class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0 for _ in range(cols)]
        max_area = 0

        for row in matrix:
            for i, num in enumerate(row):
                heights[i] = heights[i] + 1 if num == 1 else 0
            max_area = max(max_area, self.find_max_rectangle(heights, cols))

        return max_area

    def find_max_rectangle(self, heights, n):
        stack = []
        max_area = 0

        for i, height in enumerate(heights + [-1]):
            while stack and heights[stack[-1]] >= height:
                prev = heights[stack.pop()]

                side = (i - stack[-1] - 1) if stack else i

                max_area = max(max_area, prev * side)
            stack.append(i)

        return max_area
