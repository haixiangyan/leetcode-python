class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        i, j = 0, 0
        A_length, B_length = len(A), len(B)
        result = []

        while i < A_length and j < B_length:
            if A[i] < B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1

        while i < A_length:
            result.append(A[i])
            i += 1

        while j < B_length:
            result.append(B[j])
            j += 1

        return result
