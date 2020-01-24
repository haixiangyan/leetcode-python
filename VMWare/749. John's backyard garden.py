class Solution:
    """
    @param x: the wall's height
    @return: YES or NO
    """
    def isBuild(self, x):
        bricks = [3, 7]

        dp = [False for _ in range(x + 1)]
        dp[0] = True

        for height in range(1, x + 1):
            for brick in bricks:
                if height - brick < 0:
                    continue
                dp[height] = dp[height] or dp[height - brick]

        return 'YES' if dp[-1] else 'NO'
