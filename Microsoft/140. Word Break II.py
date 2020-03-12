class Solution:
    def wordBreak(self, s: str, wordDict):
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return []

        parts = []

        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue

            sub_parts = self.dfs(s[i:], wordDict, memo)
            for sub_part in sub_parts:
                parts.append(prefix + ' ' + sub_part)

        if s in wordDict:
            parts.append(s)

        memo[s] = parts
        return parts
