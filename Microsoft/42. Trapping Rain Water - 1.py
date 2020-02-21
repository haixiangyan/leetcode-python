class Solution:
    def trap(self, heights) -> int:
        if not heights:
            return 0

        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]
        water = 0

        while left < right:
            if heights[left] < heights[right]:
                left_max = max(left_max, heights[left])
                water += left_max - heights[left]
                left += 1
            else:
                right_max = max(right_max, heights[right])
                water += right_max - heights[right]
                right -= 1

        return water
