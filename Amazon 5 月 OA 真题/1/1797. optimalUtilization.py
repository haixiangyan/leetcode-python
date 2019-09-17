class Solution:
    """
    @param A: a integer sorted array
    @param B: a integer sorted array
    @param K: a integer
    @return: return a pair of index
    """
    def optimalUtilization(self, A, B, K):
        if not A or not B:
            return [0, 0]

        indexA, indexB = 0, 0
        for i in range(len(A)):
            curtSum = A[indexA] + B[indexB]

            for j in range(len(B)):
                if A[i] + B[j] == K:
                    return [i, j]
                elif A[i] + B[j] < K:
                    if A[i] + B[j] > curtSum:
                        indexA, indexB = i, j
                        curtSum = A[indexA] + B[indexB]
                else:
                    break

        return [indexA, indexB]
