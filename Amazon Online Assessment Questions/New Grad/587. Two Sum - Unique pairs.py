class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if not nums:
            return 0

        nums, n = sorted(nums), len(nums)
        left, right = 0, n - 1
        count = 0

        while left < right:
            curtSum = nums[left] + nums[right]

            if curtSum < target:
                left += 1
            elif curtSum > target:
                right -= 1
            else:
                count += 1
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

        return count
