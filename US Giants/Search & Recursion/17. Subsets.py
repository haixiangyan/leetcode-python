class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
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
            temp.append(nums[i])
            self.dfs(nums, i + 1, length, temp)
            temp.pop()
