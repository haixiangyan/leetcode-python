class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        n = len(nums)
        if not nums or k <= 0 or n < k:
            return []

        sums = [0 for _ in range(n - k + 1)]
        for i in range(k):
            sums[0] += nums[i]

        for i in range(1, n - k + 1):
            sums[i] = sums[i - 1] + nums[i + k - 1] - nums[i - 1]

        return sums
