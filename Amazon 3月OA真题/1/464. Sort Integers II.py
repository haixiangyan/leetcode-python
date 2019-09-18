class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):
        if not A:
            return

        self.quicksort(A, 0, len(A) - 1)

        return A

    def quicksort(self, A, start, end):
        if start >= end:
            return

        pivot = A[(start + end) // 2]
        left, right = start, end

        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and pivot < A[right]:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        self.quicksort(A, start, right)
        self.quicksort(A, left, end)
