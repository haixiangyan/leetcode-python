import math
class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        if n == 1:
            return []

        return self.dfs(n, {})

    def dfs(self, n, memo):
        if n in memo:
            return memo[n]

        factors = []

        for factor in range(2, int(math.sqrt(n)) + 1):
            if n % factor == 0:
                prefix = factor
                factors.append([prefix, n // factor]) # 小，大

                sub_factors = self.dfs(n // factor, memo)
                for sub in sub_factors:
                    if prefix > sub[0]:
                        continue
                    factors.append([prefix] + sub)

        memo[n] = factors
        return factors
