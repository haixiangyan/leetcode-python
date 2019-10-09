class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        if len(A) != len(B):
            return False
        storeA = {}
        storeB = {}
        n = len(A)

        for i in range(n):
            # A
            if A[i] not in storeA:
                storeA[A[i]] = 0
            storeA[A[i]] += 1

            # B
            if B[i] not in storeB:
                storeB[B[i]] = 0
            storeB[B[i]] += 1
        
        for char in storeA:
            if char not in storeB or storeA[char] != storeB[char]:
                return False
            
        return True