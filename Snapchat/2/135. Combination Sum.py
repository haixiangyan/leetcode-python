class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        if not candidates:
            return []

        candidates = sorted(list(set(candidates)))
        results = []

        self.dfs(candidates, 0, target, [], results)

        return results

    def dfs(self, candidates, index, target, combination, results):
        if target < 0:
            return
        if target == 0:
            return results.append(list(combination))

        for i in range(index, len(candidates)):
            combination.append(candidates[i])
            self.dfs(candidates, i, target - candidates[i], combination, results)
            combination.pop()
