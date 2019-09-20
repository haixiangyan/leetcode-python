def maximumTotalWeight(weights, tasks, p):
    dp = [[0 for _ in range(p // 2 + 1)] for _ in range(len(tasks) + 1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if j < tasks[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - tasks[i - 1]] + weights[i - 1])

    return dp[len(tasks)][p // 2]