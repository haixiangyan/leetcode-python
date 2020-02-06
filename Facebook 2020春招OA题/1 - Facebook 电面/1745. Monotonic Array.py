class Solution:
    """
    @param A: a array
    @return: is it monotonous
    """
    def isMonotonic(self, A):
        if not A or len(A) == 1:
            return True

        increase = decrease = True
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                increase = False

            if A[i] < A[i + 1]:
                decrease = False

            if not increase and not decrease:
                return False

        return True
