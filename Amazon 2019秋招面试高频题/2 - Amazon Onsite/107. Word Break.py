class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dictonary):
        if len(dictonary) == 0:
            return s == ''

        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        max_length = max([len(word) for word in dictonary])

        for i in range(1, len(s) + 1):
            for j in range(1, min(i, max_length) + 1):
                if not dp[i - j]:
                    continue
                if s[i - j:i] in dictonary:
                    dp[i] = True
                    break

        return dp[-1]
