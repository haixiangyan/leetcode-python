class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        if nums is None:
            return

        left, right = 0, len(nums) - 1

        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1

            if left <= right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp

        return left
