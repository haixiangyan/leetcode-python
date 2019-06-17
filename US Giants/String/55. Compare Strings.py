class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        if A is None or B is None:
            return False
        
        AChars = ''.join(A)
        BChars = ''.join(B)
        
        ACharset = [0] * 256
        BCharset = [0] * 256
        
        for i in range(len(AChars)):
            ACharset[ord(AChars[i])] += 1
            
        for i in range(len(BChars)):
            BCharset[ord(BChars[i])] += 1
            
        for i in range(0, 256):
            if BCharset[i] > ACharset[i]:
                return False
                
        return True