class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """

    def searchInsert(self, A, target):
        if A is None or len(A) == 0:
            return 0

        left, right = 0, len(A) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if A[mid] > target:
                right = mid
            elif A[mid] < target:
                left = mid
            else:
                return mid

        if A[left] >= target:
            return left
        if A[right] >= target:
            return right
        return len(A)
