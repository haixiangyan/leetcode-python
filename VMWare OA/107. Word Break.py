class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, word_dict):
        if len(word_dict) == 0:
            return s == ''

        n = len(s)

        dp = [False for _ in range(n + 1)]
        dp[0] = True

        max_len = max([len(word) for word in word_dict])

        for i in range(1, n + 1):
            for j in range(1, min(i, max_len) + 1):
                if not dp[i - j]:
                    continue

                if s[i - j:i] in word_dict:
                    dp[i] = True
                    break

        return dp[-1]
