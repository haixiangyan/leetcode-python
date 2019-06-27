class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        max_length = 0
        for i in range(len(A)):
            for j in range(len(B)):
                length = 0
                while i + length < len(A) and j + length < len(B) and A[i + length] == B[j + length]:
                    length += 1
                if length > max_length:
                    max_length = length

        return max_length
