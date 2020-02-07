class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: return an integer
    """
    def longestSubstring(self, s, k):
        for char in s:
            if s.count(char) < k:
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(char))
        return len(s)
