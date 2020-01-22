class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        candidates = sorted(list(set(candidates)))
        combinations = []

        self.dfs([], target, 0, candidates, combinations)

        return combinations

    def dfs(self, curt, target, index, candidates, combinations):
        if target < 0:
            return

        if target == 0:
            combinations.append(curt[:])
            return

        for i in range(index, len(candidates)):
            curt.append(candidates[i])
            self.dfs(curt, target - candidates[i], i, candidates, combinations)
            curt.pop()
