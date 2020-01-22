class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        if not coins:
            return amount == 0

        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for curt in range(1, amount + 1):
            for coin in coins:
                if curt - coin < 0:
                    continue

                dp[curt] = min(dp[curt], dp[curt - coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1
