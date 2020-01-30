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
        n, m = len(A), len(B)
        i, j = 0, 0
        results = []

        for _ in range(n + m):
            if i < n and (j >= m or A[i] < B[j]):
                results.append(A[i])
                i += 1
            else:
                results.append(B[j])
                j += 1

        return results
