class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})


    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return []

        partitions = []
        for i in range(1, len(s)):
            prefix = s[:i]

            if prefix not in wordDict:
                continue

            sub_parts = self.dfs(s[i:], wordDict, memo)
            for sub in sub_parts:
                partitions.append(prefix + ' ' + sub)

        if s in wordDict:
            partitions.append(s)

        memo[s] = partitions
        return partitions
