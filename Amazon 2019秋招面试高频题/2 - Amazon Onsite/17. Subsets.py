class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        nums = sorted(nums)
        results = []

        self.dfs(nums, 0, results, [])

        return results

    def dfs(self, nums, index, results, curt):
        results.append(curt[:])

        for i in range(index, len(nums)):
            curt.append(nums[i])
            self.dfs(nums, i + 1, results, curt)
            curt.pop()
