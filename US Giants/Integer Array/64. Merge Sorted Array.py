class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        total_index = m + n - 1
        A_index = m - 1
        B_index = n - 1

        while A_index >= 0 and B_index >= 0:
            if A[A_index] >= B[B_index]:
                A[total_index] = A[A_index]
                A_index -= 1
                total_index -= 1
            if B[B_index] > A[A_index]:
                A[total_index] = B[B_index]
                B_index -= 1
                total_index -= 1

        while A_index >= 0:
            A[total_index] = A[A_index]
            A_index -= 1
            total_index -= 1

        while B_index >= 0:
            A[total_index] = B[B_index]
            B_index -= 1
            total_index -= 1
