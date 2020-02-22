class Solution:
    def generateParenthesis(self, n: int):
        results = []

        self.dfs(n, n, '', results)

        return results

    def dfs(self, left, right, curt, results):
        if right < left:
            return

        if left == 0 and right == 0:
            results.append(curt)

        if left > 0:
            self.dfs(left - 1, right, curt + '(', results)

        if right > 0:
            self.dfs(left, right - 1, curt + ')', results)
