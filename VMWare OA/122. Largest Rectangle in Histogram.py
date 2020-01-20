class Solution:
    """
    @param heights: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, heights):
        if not heights:
            return 0

        max_area = 0
        n = len(heights)
        stack = []

        for i in range(n + 1):
            curt = -1 if i == n else heights[i]
            while stack and heights[stack[-1]] >= curt:
                prev_height = heights[stack.pop()]

                side = (i - stack[-1] - 1) if stack else i

                max_area = max(max_area, prev_height * side)

            stack.append(i)

        return max_area
