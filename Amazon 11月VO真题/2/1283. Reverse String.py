class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverseString(self, s):
        result = ''

        for i in range(len(s) - 1, -1, -1):
            result += s[i]

        return result
