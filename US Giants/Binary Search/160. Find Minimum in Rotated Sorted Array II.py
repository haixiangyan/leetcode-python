class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return min(nums[left], nums[right])
