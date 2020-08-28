from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        key, count = None, 0

        for num in nums:
            if count == 0:
                key, count = num, 1
            elif key == num:
                count += 1
            else:
                count -= 1
        
        return key
