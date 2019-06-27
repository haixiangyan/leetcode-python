class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        end = 0
        min_length = min([len(str) for str in strs])

        while end < min_length:
            for i in range(1, len(strs)):
                if strs[i - 1][end] != strs[i][end]:
                    return strs[0][:end]
            end += 1

        return strs[0][:end]
