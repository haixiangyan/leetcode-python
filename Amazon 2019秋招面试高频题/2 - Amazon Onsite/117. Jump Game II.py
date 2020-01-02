class Solution:
    def __init__(self):
        self.min_jump = float('inf')
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        if not A or len(A) == 0:
            return -1

        start, end, jumps = 0, 0, 0

        while end < len(A) - 1:
            jumps += 1

            farthest = end
            for i in range(start, end + 1):
                if A[i] + i > farthest:
                    farthest = A[i] + i

            start = end + 1
            end = farthest

        return jumps
