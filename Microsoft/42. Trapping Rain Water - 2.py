class Solution:
    def trap(self, heights) -> int:
        if not heights:
            return 0

        stack = []
        water = 0
        for right, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                ground = heights[stack.pop()]

                if not stack:
                    continue

                left = stack[-1]
                water_line = min(heights[left], height)
                water += (water_line - ground) * (right - left - 1)
            stack.append(right)

        return water
