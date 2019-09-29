class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        if not num:
            return []

        num = sorted(num)
        self.results, temp, visited = [], [], [0] * len(num)
        self.dfs(num, target, 0, 0, temp, visited)
        return self.results

    def dfs(self, nums, target, index, curt, temp, visited):
        if curt == target:
            self.results.append(list(temp))
            return

        for i in range(index, len(nums)):
            if curt + nums[i] <= target and (i == 0 or nums[i] != nums[i - 1] or visited[i - 1] == 1):
                temp.append(nums[i])
                visited[i] = 1
                self.dfs(nums, target, i + 1, curt + nums[i], temp, visited)
                visited[i] = 0
                temp.pop()
