class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        if not candidates:
            return []

        candidates = sorted(set(candidates))

        self.results = []

        self.dfs(candidates, 0, [], target)

        return self.results


    def dfs(self, candidates, index, path, target):
        if target < 0:
            return
        if target == 0:
            self.results.append(path[:])
            return
        if index >= len(candidates):
            return

        for i in range(index, len(candidates)):
            path.append(candidates[i])
            self.dfs(candidates, i, path, target - candidates[i])
            path.pop()