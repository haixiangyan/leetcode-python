class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2

            if A[mid] < A[mid + 1]:
                left = mid
            else:
                right = mid

        if A[right] > A[left]:
            return right
        else:
            return left
