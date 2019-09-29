class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        sLen, tLen = len(s), len(t)

        if abs(sLen - tLen) > 1:
            return False

        if sLen > tLen:
            return self.isOneEditDistance(t, s)

        for i in range(sLen):
            if s[i] != t[i]:
                if sLen == tLen:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]

        return sLen != tLen
