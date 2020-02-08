class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        results = []

        self.dfs(sorted(A), 0, [], k, target, results)

        return results

    def dfs(self, A, index, curt, k, target, results):
        if len(curt) == k:
            if target == 0:
                results.append(curt[:])
            return

        for i in range(index, len(A)):
            curt.append(A[i])
            self.dfs(A, i + 1, curt, k, target - A[i], results)
            curt.pop()
