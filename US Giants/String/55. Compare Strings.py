class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        if A is None or B is None:
            return False
        
        A_chars = [0] * 256
        B_chars = [0] * 256
        
        for char in A:
            A_chars[ord(char)] += 1
        
        for char in B:
            B_chars[ord(char)] += 1
            
        for i in range(256):
            if A_chars[i] < B_chars[i]:
                return False
                
        return True
