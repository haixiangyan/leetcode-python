class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):

        if len(nums) == 0:
            return 0
        
        global_max = prev_max = prev_min = nums[0]

        for num in nums[1:]:
            if num > 0:
                curt_max = max(num, prev_max * num)
                curt_min = min(num, prev_min * num)
            else:
                curt_max = max(num, prev_min * num)
                curt_min = min(num, prev_max * num)

            global_max = max(global_max, curt_max)
            prev_max, prev_min = curt_max, curt_min

        return global_max