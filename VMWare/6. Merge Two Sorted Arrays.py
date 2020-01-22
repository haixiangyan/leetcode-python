class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        i1, i2 = 0, 0
        m, n = len(A), len(B)
        results = []

        while i1 < m and i2 < n:
            if A[i1] < B[i2]:
                results.append(A[i1])
                i1 += 1
            else:
                results.append(B[i2])
                i2 += 1

        while i1 < m:
            results.append(A[i1])
            i1 += 1
        while i2 < n:
            results.append(B[i2])
            i2 += 1

        return results