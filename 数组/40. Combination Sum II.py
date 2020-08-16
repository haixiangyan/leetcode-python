from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        results = []

        nums = sorted(candidates)
        visited = [0 for _ in range(len(candidates))]

        self.dfs(nums, visited, 0, target, [], results)

        return results

    def dfs(self, nums, visited, index, target, path, results):
        if target < 0:
            return
        
        if target == 0:
            results.append(path[:])
            return

        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            path.append(nums[i])
            visited[i] = 1
            self.dfs(nums, visited, i + 1, target - nums[i], path, results)
            visited[i] = 0
            path.pop()
