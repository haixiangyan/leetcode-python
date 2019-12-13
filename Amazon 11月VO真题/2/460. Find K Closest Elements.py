class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        right = self.find_upperbound(A, target)
        left = right - 1

        results = []

        for _ in range(k):
            if self.is_left_closer(A, target, left, right):
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1

        return results

    def find_upperbound(self, A, target):
        left, right = 0, len(A) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] < target:
                left = mid
            else:
                right = mid

        if A[left] >= target:
            return left
        if A[right] >= target:
            return right

        return right + 1

    def is_left_closer(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
