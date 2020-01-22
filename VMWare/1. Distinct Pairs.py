class Solution:
    def distinct_pairs(self, nums, target):
        counts = 0
        if not nums:
            return counts

        sorted_nums = sorted(nums)
        left, right = 0, len(sorted_nums) - 1

        while left < right:
            if sorted_nums[left] + sorted_nums[right] > target:
                right -= 1
            elif sorted_nums[left] + sorted_nums[right] < target:
                left += 1
            else:
                # Add pair
                counts += 1
                # Move left and right to the center of array
                left += 1
                right -= 1

                # Skip duplicate number on left hand side
                while left < right and sorted_nums[left - 1] == sorted_nums[left]:
                    left += 1
                # Skip duplicate number on right hand side
                while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                    right -= 1

        return counts


s = Solution()
# 3
nums = [5, 7, 9, 13, 11, 6, 6, 3, 3]
print(s.distinct_pairs(nums, 12))

# 2
nums = [6, 6, 3, 9, 3, 5, 1]
print(s.distinct_pairs(nums, 12))
