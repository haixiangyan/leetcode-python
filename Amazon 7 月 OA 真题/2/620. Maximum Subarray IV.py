class Solution:
    """
    @param nums: an array of integer
    @param k: an integer
    @return: the largest sum
    """
    def maxSubarray4(self, nums, k):
        n = len(nums)

        if n < k:
            return 0

        sums = [0 for _ in range(n + 1)]

        result = 0
        for i in range(k):
            result += nums[i]

        prefixMinSum = 0
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

            if i >= k and sums[i] - prefixMinSum > result:
                result = sums[i] - prefixMinSum

            if i >= k:
                prefixMinSum = min(prefixMinSum, sums[i - k + 1])

        return result
