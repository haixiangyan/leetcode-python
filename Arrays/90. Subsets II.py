from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums = sorted(nums)

        path = []
        self.results = []

        self.dfs(nums, 0, len(nums), path)

        return self.results

    def dfs(self, nums, index, length, path):
        if index > length:
            return

        self.results.append(path[:])

        for i in range(index, length):
            if i > index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, length, path)
            path.pop()
