class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        if nums is None:
            return []

        if not nums:
            return [[]]

        permutations = []
        self.dfs([], sorted(nums), permutations)
        return permutations

    def dfs(self, path, nums, permutations):
        if len(nums) == 0:
            permutations.append(path[:])
            return

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            self.dfs(path + [nums[i]], nums[:i] + nums[i + 1:], permutations)
