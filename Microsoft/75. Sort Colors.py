class Solution:
    def sortColors(self, nums) -> None:
        left, right, index = 0, len(nums) - 1, 0

        while index <= right:
            if nums[index] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                left += 1
                index += 1
            elif nums[index] == 2:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
            else:
                index += 1
