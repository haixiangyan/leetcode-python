class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        if not heights:
            return 0

        left, right = 0, len(heights) - 1
        max_left, max_right = heights[left], heights[right]
        water = 0

        while left <= right:
            if heights[left] < heights[right]:
                max_left = max(max_left, heights[left])
                water += max_left - heights[left]
                left += 1
            else:
                max_right = max(max_right, heights[right])
                water += max_right - heights[right]
                right -= 1

        return water
