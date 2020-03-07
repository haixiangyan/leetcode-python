class Solution:
    def maxProduct(self, nums) -> int:
        if not nums:
            return 0

        global_max = prev_min = prev_max = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                curt_max = max(nums[i], prev_max * nums[i])
                curt_min = min(nums[i], prev_min * nums[i])
            else:
                curt_max = max(nums[i], prev_min * nums[i])
                curt_min = min(nums[i], prev_max * nums[i])

            global_max = max(global_max, curt_max)
            prev_max, prev_min = curt_max, curt_min
        return global_max
