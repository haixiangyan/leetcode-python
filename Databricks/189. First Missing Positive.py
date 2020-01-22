class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """

    def firstMissingPositive(self, A):
        if not A:
            return 1

        n = len(A)
        for i in range(n):
            while A[i] != i + 1 and 0 < A[i] <= n and A[i] != A[A[i] - 1]:
                t = A[i]
                A[i] = A[A[i] - 1]
                A[t - 1] = t

        for i, num in enumerate(A):
            if i + 1 != num:
                return i + 1

        return n + 1
