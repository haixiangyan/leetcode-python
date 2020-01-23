class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        nums = sorted(nums)
        left, right = 0, len(nums) - 1
        counts = 0
        while left < right:
            curt_sum = nums[left] + nums[right]
            if curt_sum < target:
                left += 1
            elif curt_sum > target:
                right -= 1
            else:
                counts += 1
                left += 1
                right -= 1

                while left < right and nums[left - 1] == nums[left]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

        return counts
