class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, max_size, sizes, values):
        n = len(sizes)

        dp = [[0 for _ in range(max_size + 1)] for _ in range(n + 1)]

        # Initialize
        for size in range(1, max_size + 1):
            dp[0][size] = -1

        for item in range(1, n + 1):
            for size in range(1, max_size + 1):
                dp[item][size] = dp[item - 1][size]
                if size >= sizes[item - 1] and dp[item - 1][size - sizes[item - 1]] != -1:
                    dp[item][size] = max(dp[item][size], dp[item - 1][size - sizes[item - 1]] + values[item - 1])

        return max(dp[n])
