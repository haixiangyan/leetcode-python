class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        sum = 0
        min_sum = nums[0]
        max_sum = 0

        for i in range(len(nums)):
            sum += nums[i]

            if sum - max_sum < min_sum:
                min_sum = sum - max_sum
            if sum > max_sum:
                max_sum = sum

        return min_sum