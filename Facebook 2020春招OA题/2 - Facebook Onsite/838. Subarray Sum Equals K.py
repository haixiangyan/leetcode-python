class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """

    def subarraySumEqualsK(self, nums, k):
        if not nums:
            return 0

        # 计算 presum
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]

        counts = {0: 1}
        result = 0
        # x - y = k
        # 遍历存 y 值，找 x 值
        for i in range(len(nums)):
            if nums[i] not in counts:
                counts[nums[i]] = 1
            else:
                counts[nums[i]] += 1
            if nums[i] - k in counts:
                result += counts[nums[i] - k]

        return result
