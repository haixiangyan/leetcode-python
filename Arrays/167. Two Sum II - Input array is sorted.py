from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            cur_sum = numbers[left] + numbers[right]

            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        
        return []
