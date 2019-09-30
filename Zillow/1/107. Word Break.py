class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dictionary):
        if len(dictionary) == 0:
            return len(s) == 0

        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True

        maxLength = max([len(w) for w in dictionary])
        for i in range(1, n + 1):
            for j in range(1, min(maxLength, i) + 1):
                if not dp[i - j]:
                    continue
                
                if s[i - j:i] in dictionary:
                    dp[i] = True
                    break

        return dp[n]