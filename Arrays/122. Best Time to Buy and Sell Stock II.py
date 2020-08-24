from typing import List


class Solution:
    # 只能买卖一次，相加差值就好了
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                profit += prices[i] - prices[i - 1]

        return profit
