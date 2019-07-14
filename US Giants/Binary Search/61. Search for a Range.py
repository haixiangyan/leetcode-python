class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        if A is None or len(A) == 0:
            return [-1, -1]

        lower_bound = self.find_lower_bound(A, target)
        upper_bound = self.find_upper_bound(A, target)

        return [lower_bound, upper_bound]

    def find_lower_bound(self, A, target):
        left, right = 0, len(A) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if A[mid] < target:
                left = mid
            else:
                right = mid

        if A[left] == target:
            return left
        if A[right] == target:
            return right

        return -1

    def find_upper_bound(self, A, target):
        left, right = 0, len(A) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if A[mid] > target:
                right = mid
            else:
                left = mid

        if A[right] == target:
            return right
        if A[left] == target:
            return left

        return -1
