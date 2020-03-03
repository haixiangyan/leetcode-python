class Solution:
    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []

        nums = sorted(nums)
        results = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            self.two_sum(nums, i + 1, n - 1, -nums[i], results)

        return results

    def two_sum(self, nums, left, right, target, results):
        while left < right:
            curt_sum = nums[left] + nums[right]
            if curt_sum < target:
                left += 1
            elif curt_sum > target:
                right -= 1
            else:
                results.append([-target, nums[left], nums[right]])
                left, right = left + 1, right - 1

                while left < right and nums[left - 1] == nums[left]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
