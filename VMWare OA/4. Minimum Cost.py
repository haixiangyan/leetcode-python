class Solution:
    def min_cost(self, nums):
        if not nums:
            return 0

        increase_nums = sorted(nums)
        decrease_nums = sorted(nums, reverse=True)

        # Try increase and decrease 2 times, and check which one is the lowest cost
        return min(self.get_cost(nums, increase_nums), self.get_cost(nums, decrease_nums))

    def get_cost(self, nums, sorted_nums):
        n = len(sorted_nums)

        # Row: original number array
        # Col: sorted number array
        # dp[i][j] represents the minimum cost before ith element, based on sorted jth element
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = abs(sorted_nums[0] - nums[0])
                elif i == 0:
                    dp[0][j] = min(dp[0][j - 1], abs(sorted_nums[j] - nums[0]))
                elif j == 0:
                    dp[i][0] = dp[i - 1][0] + abs(sorted_nums[0] - nums[i])
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j] + abs(sorted_nums[j] - nums[i]))

        return dp[-1][-1]

s = Solution()
nums = [1, 2, 6, 3, 5]
print(s.min_cost(nums))
