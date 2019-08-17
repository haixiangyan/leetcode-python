class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        num = sorted(num)
        self.results = []
        temp = []
        visited = [False] * len(num)

        self.dfs(num, target, 0, 0, temp, visited)

        return self.results

    def dfs(self, num, target, p, now, temp, visited):
        if now == target:
            self.results.append(temp[:])
            return

        for i in range(p, len(num)):
            if now + num[i] <= target and (i == 0 or num[i] != num[i - 1] or visited[i - 1]):
                temp.append(num[i])
                visited[i] = True
                self.dfs(num, target, i + 1, now + num[i], temp, visited)
                temp.pop()
                visited[i] = False
