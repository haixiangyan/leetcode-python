class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        if s is None or t is None:
            return False
            
        s_chars = [0] * 256
        t_chars = [0] * 256
        
        for char in s:
            s_chars[ord(char)] += 1
        
        for char in t:
            t_chars[ord(char)] += 1
            
        for i in range(256):
            if s_chars[i] != t_chars[i]:
                return False
        
        return True