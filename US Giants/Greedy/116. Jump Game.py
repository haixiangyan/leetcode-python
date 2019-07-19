class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        if A is None or len(A) == 0:
            return False

        max_jump = A[0]
        for i in range(len(A)):
            if max_jump >= i and A[i] + i >= max_jump:
                max_jump = A[i] + i

        return max_jump >= len(A) + 1
