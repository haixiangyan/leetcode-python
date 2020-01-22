class Solution:
    """
    @param A: a integer sorted array
    @param B: a integer sorted array
    @param K: a integer
    @return: return a pair of index
    """
    def optimalUtilization(self, A, B, K):
        if not A or not B:
            return []

        optimal = A[0] + B[0]
        left, right = 0, len(B) - 1
        result = []

        while left < len(A) and right >= 0:
            while right >= 0 and A[left] + B[right] > K or right - 1 >= 0 and B[right] == B[right - 1]:
                right -= 1

            if A[left] + B[right] <= K:
                if A[left] + B[right] > optimal:
                    optimal = A[left] + B[right]
                    result = [left, right]
            left += 1

        return result
