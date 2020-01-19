class Solution:
    def permute(self, nums):
        if nums is None:
            return []

        if not nums:
            return [[]]

        nums = sorted(nums)
        results = []
        self.dfs(nums, [], results)
        return results

    def dfs(self, nums, curt, results):
        if nums == []:
            results.append(curt[:])

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], curt + [nums[i]], results)
