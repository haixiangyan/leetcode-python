class Solution:
    """
    @param A: a integer sorted array
    @param B: a integer sorted array
    @param K: a integer
    @return: return a pair of index
    """
    def optimalUtilization(self, A, B, K):
        if not A or not B:
            return [-1, -1]

        index_a, index_b = 0, 0

        for i in range(len(A)):
            optimal = A[index_a] + B[index_b]
            for j in range(len(B)):
                curt_sum = A[i] + B[j]
                if curt_sum == K:
                    return [i, j]
                elif curt_sum < K:
                    if curt_sum > optimal:
                        index_a, index_b = i, j
                        optimal = curt_sum
                else:
                    break

        return [index_a, index_b]