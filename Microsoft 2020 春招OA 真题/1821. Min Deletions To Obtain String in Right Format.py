class Solution:
    """
    @param s: the string
    @return: Min Deletions To Obtain String in Right Format
    """
    def minDeletionsToObtainStringInRightFormat(self, s):
        rhs = lhs = 0

        for i in range(len(s)):
            if s[i] == 'A':
                rhs += 1

        result = rhs

        for i in range(len(s)):
            if s[i] == 'A':
                rhs -= 1
            else:
                lhs += 1
            result = min(result, rhs + lhs)
        return result
