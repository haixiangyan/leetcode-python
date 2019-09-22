class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        if not nums:
            return []
        prefixSums = [0 for _ in range(len(nums) + 1)]

        for i in range(len(nums)):
            prefixSums[i + 1] = prefixSums[i] + nums[i]

        results = []
        for i in range(k, len(nums) + 1):
            results.append(prefixSums[i] - prefixSums[i - k])

        return results
