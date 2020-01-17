class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        index_a, index_b = m - 1, n - 1
        position = m + n - 1

        while index_a >= 0 and index_b >= 0:
            if A[index_a] > B[index_b]:
                A[position] = A[index_a]
                position -= 1
                index_a -= 1
            else:
                A[position] = B[index_b]
                position -= 1
                index_b -= 1

        while index_a >= 0:
            A[position] = A[index_a]
            position -= 1
            index_a -= 1

        while index_b >= 0:
            A[position] = B[index_b]
            position -= 1
            index_b -= 1
