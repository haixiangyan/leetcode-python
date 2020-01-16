class Solution:
    def countSubarrays(self, nums, m):
        count = 0

        for i in range(len(nums)):
            odds = 0
            for j in range(i, len(nums)):
                if nums[j] % 2 == 1:
                    odds += 1

                if odds == m:
                    count += 1

        return count

s = Solution()
nums = [2, 2, 5, 6, 9, 2, 11]
m = 2
print(s.countSubarrays(nums, m))
