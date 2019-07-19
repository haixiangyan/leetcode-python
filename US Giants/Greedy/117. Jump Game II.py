class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        if A is None or len(A) == 0:
            return float('inf')

        if len(A) == 1:
            return 0

        start, end = 0, 0
        steps = 0

        while end < len(A) - 1:
            further_step = 0
            steps += 1

            for i in range(start, end + 1):
                further_step = max(further_step, A[i] + i)

                # Already reached end point
                if further_step >= len(A) - 1:
                    return steps

            start = end + 1
            end = further_step

            if start > end:
                break

        return float('inf')
