class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        store = {}
        for char in s:
            if char in store:
                del store[char]
            else:
                store[char] = True
        
        size = len(store)
        if size <= 1:
            return len(s)
        else:
            return len(s) - size + 1
