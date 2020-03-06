class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s, set_t = [0] * 256, [0] * 256
        for i in range(len(s)):
            set_s[ord(s[i])] += 1
        for i in range(len(t)):
            set_t[ord(t[i])] += 1
        for i in range(256):
            if set_s[i] != set_t[i]:
                return False
        return True
