class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs(s, 0, p, 0, {})

    def dfs(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # Source 到头了，pattern 后面一定要是 *
        if i == len(source):
            for index in range(j, len(pattern)):
                if pattern[index] != '*':
                    return False
            return True

        # Pattern 到头了，此时 source 还没到头，返回 False
        if j == len(pattern):
            return False

        if pattern[j] != '*':
            matched = self.match_char(source[i], pattern[j]) and self.dfs(source, i + 1, pattern, j + 1, memo)
        else:
            matched = self.dfs(source, i + 1, pattern, j, memo) or self.dfs(source, i, pattern, j + 1, memo)

        memo[(i, j)] = matched
        return matched

    def match_char(self, s, p):
        return s == p or p == '?'
