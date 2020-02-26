class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0

        min_price, max_profit = float('inf'), 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
