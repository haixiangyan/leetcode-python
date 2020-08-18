from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return 0

        nums = sorted(nums)
        closest = float('inf')
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                if abs(cur_sum - target) < abs(closest - target):
                    closest = cur_sum

                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    return cur_sum
        return closest
