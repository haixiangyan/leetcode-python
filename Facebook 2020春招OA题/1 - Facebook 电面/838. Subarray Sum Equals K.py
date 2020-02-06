class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        n = len(nums)
        prefix_sum = [0 for _ in range(n)]
        prefix_sum[0] = nums[0]

        store = {0: 1}
        results = 0

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        for ps in prefix_sum:
            if k + ps in store:
                results += store[k - ps]

            if ps not in store:
                store[ps] = 0
            store[ps] += 1

        return results
