class Solution:
    def getMinSum(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        nums = sorted(nums)

        min_sum, curt_max = nums[0], nums[0]

        for i in range(1, len(nums)):
            if curt_max >= nums[i]:
                curt_max += 1
                min_sum += curt_max
            else:
                min_sum += nums[i]
                curt_max = nums[i]

        return min_sum

s = Solution()
nums = [1, 2, 2, 4, 5]
print(s.getMinSum(nums))
