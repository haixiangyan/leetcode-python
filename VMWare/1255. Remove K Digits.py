class Solution:
    """
    @param num: a string
    @param k: an integer
    @return: return a string
    """
    def removeKdigits(self, nums, k):
        if not nums:
            return 0

        if k > len(nums):
            return 0

        results = []
        for i in range(len(nums)):
            while len(results) > 0 and k > 0 and results[-1] > nums[i]:
                results.pop()
                k -= 1
            if len(results) > 0 or nums[i] != '0':
                results.append(nums[i])

        while len(results) > 0 and k > 0:
            results.pop()
            k -= 1

        if len(results) == 0:
            return '0'

        return ''.join(results)
