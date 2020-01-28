class Solution:
    """
    @param nums: the given array
    @param k: the window size
    @return: the sum of the count of unique elements in each window
    """
    def slidingWindowUniqueElementsSum(self, nums, k):
        if not nums:
            return 0

        n = len(nums)
        k = k if k <= n else n
        window = {}
        result = 0
        uniques = 0

        for i in range(k):
            if nums[i] not in window:
                window[nums[i]] = 1
                uniques += 1
            else:
                if window[nums[i]] == 1:
                    uniques -= 1
                window[nums[i]] += 1
        result += uniques

        for i in range(k, n):
            prev_num = nums[i - k]
            window[prev_num] -= 1

            # prev_num
            if window[prev_num] == 1: # Unique again
                uniques += 1
            elif window[prev_num] == 0: # Not unique
                uniques -= 1

            if nums[i] not in window or window[nums[i]] == 0: # Unique again
                window[nums[i]] = 1
                uniques += 1
            else:
                if window[nums[i]] == 1: # Not unique
                    uniques -= 1
                window[nums[i]] += 1
            result += uniques
        return result

