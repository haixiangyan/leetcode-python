import math


class Solution:
    def getArray(self, A, target):
        dp = [100000.0 for _ in range(target + 1)]
        path = [[0 for _ in range(len(A) + 1)] for _ in range(target + 1)]
        results = [0 for _ in range(len(A))]

        n = len(A)
        dp[0] = 0.0

        for i in range(n):
            for j in range(target, -1, -1):
                x, y = math.floor(A[i]), math.ceil(A[i])
                if j < x and j < y:
                    break
                if j >= x and j >= y:
                    if dp[j - x] + A[i] - x < dp[j - y] + y - A[i]:
                        dp[j] = dp[j - x] + A[i] - x
                        path[j][i] = 1
                    else:
                        dp[j] = dp[j - y] + y - A[i]
                        path[j][i] = 2
                elif j >= x:
                    dp[j] = dp[j - x] + A[i] - x
                    path[j][i] = 1
                elif j >= y:
                    dp[j] = dp[j - y] + y - A[i]
                    path[j][i] = 2

        if dp[target] >= 10000:
            return results
        else:
            curtTarget = target
            for i in range(n - 1, -1, -1):
                if path[curtTarget][i] == 1:
                    results[i] = math.floor(A[i])
                    curtTarget -= math.floor(A[i])
                elif path[curtTarget][i] == 2:
                    results[i] = math.ceil(A[i])
                    curtTarget -= math.ceil(A[i])

        return results
