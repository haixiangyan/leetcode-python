class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def __init__(self):
        self.results = []

    def permute(self, nums):
        if nums is None:
            return []
        if not nums:
            return [[]]

        self.dfs([], sorted(nums))

        return self.results

    def dfs(self, path, nums):
        if not nums:
            self.results += [path]

        for i in range(len(nums)):
            self.dfs(path + [nums[i]], nums[:i] + nums[i + 1:])
