class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices:
            return 0

        dp = [0 for _ in range(len(prices))]
        result = 0

        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1] + prices[i] - prices[i - 1], prices[i] - prices[i - 1])
            result = max(result, dp[i])

        return result
