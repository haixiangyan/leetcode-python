class Solution:
    """
    @param nums:  a sorted integer array without duplicates
    @return: the summary of its ranges
    """

    def summaryRanges(self, nums):
        if not nums:
            return nums

        nums.append(float('inf'))

        results = []
        start, end, i = 0, 0, 0

        for i in range(len(nums)):
            if i == 0:
                continue

            if nums[i - 1] + 1 == nums[i]:
                end = i
            else:
                if start == end:
                    results.append(str(nums[start]))
                else:
                    results.append(str(nums[start]) + '->' + str(nums[end]))
                start = end = i

        nums.pop()

        return results
