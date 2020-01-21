class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def findShortestSubArray(self, nums):
        if not nums:
            return 0

        first, count, result, degree = {}, {}, 0, 0
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            if num not in count:
                count[num] = 0
            count[num] += 1

            if count[num] > degree:
                degree = count[num]
                result = i - first[num] + 1
            elif count[num] == degree:
                result = min(result, i - first[num] + 1)

        return result
