class Solution:
    def distinct_pairs(self, nums, target):
        pairs = []
        if not nums:
            return pairs

        sorted_nums = sorted(nums)
        left, right = 0, len(sorted_nums) - 1

        while left < right:
            if sorted_nums[left] + sorted_nums[right] > target:
                right -= 1
            elif sorted_nums[left] + sorted_nums[right] < target:
                left += 1
            else:
                pairs.append((sorted_nums[left], sorted_nums[right]))
                left += 1
                right -= 1

                while left < right and sorted_nums[left - 1] == sorted_nums[left]:
                    left += 1
                while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                    right -= 1

        return pairs


nums = [5, 7, 9, 13, 11, 6, 6, 3, 3]
s = Solution()
print(s.distinct_pairs(nums, 12))
