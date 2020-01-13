class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        results = []

        self.dfs(0, 0, '', results, n)

        return results


    def dfs(self, left, right, curt, results, n):
        if left == n and right == n:
            results.append(curt)
            return

        if left < n:
            self.dfs(left + 1, right, curt + '(', results, n)

        if right < n and left > right:
            self.dfs(left, right + 1, curt + ')', results, n)
