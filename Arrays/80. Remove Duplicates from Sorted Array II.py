from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        index, count = 0, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[index]:
                if count < 2:
                    index += 1
                    nums[index] = nums[i]
                    count += 1
            else:
                index += 1
                nums[index] = nums[i]
                count = 1

        return index + 1
