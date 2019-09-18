class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        if not nums:
            return 0

        sortedNums = sorted(nums)

        result = 0
        left, right = 0, len(nums) - 1

        while left < right:
            curtSum = sortedNums[left] + sortedNums[right]

            if curtSum <= target:
                result += right - left
                left += 1
            else:
                right -= 1

        return result
