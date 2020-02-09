class Solution:
    """
    @param nums: an array
    @return: whether you could make one square using all the matchsticks the little match girl has
    """
    def makesquare(self, nums):
        if len(nums) < 4:
            return False

        num_sum = sum(nums)
        if num_sum % 4 != 0:
            return False

        nums = sorted(nums, reverse=True)
        targets = [num_sum / 4 for _ in range(4)]

        return self.dfs(nums, 0, targets)

    def dfs(self, nums, index, targets):
        if index == len(nums):
            return True

        for i in range(4):
            if targets[i] >= nums[index]:
                targets[i] -= nums[index]
                if self.dfs(nums, index + 1, targets):
                    return True
                targets[i] += nums[index]
        return False
