class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        self.results = []
        temp = []

        nums = sorted(nums)

        self.dfs(nums, 0, len(nums), temp)

        return self.results

    def dfs(self, nums, index, length, temp):
        if index > length:
            return

        self.results.append(temp[:])

        for i in range(index, length):
            if i > index and nums[i] == nums[i - 1]:
                continue
            temp.append(nums[i])
            self.dfs(nums, i + 1, length, temp)
            temp.pop()
