class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        if not A:
            return B
        if not B:
            return A

        results = []
        n, m = len(A), len(B)
        i, j = 0, 0

        while i < n and j < m:
            if A[i] < B[j]:
                results.append(A[i])
                i += 1
            else:
                results.append(B[j])
                j += 1

        while i < n:
            results.append(A[i])
            i += 1
        while j < m:
            results.append(B[j])
            j += 1

        return results
