from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []

        nums = sorted(nums)
        results = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.find_3_sum(nums, nums[i], i + 1, n, target - nums[i], results)

        return results

    def find_3_sum(self, nums, first, start, n, target, results):
        for i in range(start, n - 2):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.find_2_sum(nums, first, nums[i], i + 1, n - 1, target - nums[i], results)

    def find_2_sum(self, nums, first, second, left, right, target, results):
        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            else:
                results.append([first, second, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left - 1] == nums[left]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
