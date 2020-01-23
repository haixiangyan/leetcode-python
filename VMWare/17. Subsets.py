class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        sets = []
        nums = sorted(nums)

        self.dfs(nums, 0, [], sets)

        return sets

    def dfs(self, nums, start, curt, sets):
        sets.append(curt[:])

        for i in range(start, len(nums)):
            curt.append(nums[i])
            self.dfs(nums, i + 1, curt, sets)
            curt.pop()
