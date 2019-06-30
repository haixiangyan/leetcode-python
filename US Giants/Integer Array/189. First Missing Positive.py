class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """
    def firstMissingPositive(self, A):
        i = 0
        n = len(A)

        if n == 0:
            return 1

        while i < n:
            while 0 < A[i] <= n and A[i] != i + 1 and A[i] != A[A[i] - 1]:
                temp = A[i]
                A[i] = A[A[i] - 1]
                A[temp - 1] = temp

            i += 1

        for i in range(n):
            if A[i] != i + 1:
                return i + 1

        return n + 1
