class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs or len(strs) == 0:
            return ""

        for j in range(0, len(strs[0])):
            for i in range(0, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                    string = strs[i]
                    return string[0: j]

        return strs[0]
