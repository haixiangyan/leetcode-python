class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """

    def anagram(self, s, t):
        setS = [0] * 256
        setT = [0] * 256

        for i in range(len(s)):
            setS[ord(s[i])] += 1
        for i in range(len(t)):
            setT[ord(t[i])] += 1

        for i in range(0, 256):
            if setS[i] != setT[i]:
                return False
        return True
