class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        candidates = sorted(list(set(candidates)))

        self.results = []
        combination = []

        self.dfs(candidates, target, 0, combination)

        return self.results

    def dfs(self, candidates, target, start, combination):
        if target < 0:
            return
        if target == 0:
            self.results.append(combination[:])

        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination)
            combination.pop()