class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)

        if n % 2 == 1:
            return self.findKth(A, 0, B, 0, n // 2 + 1)
        else:
            smaller = self.findKth(A, 0, B, 0, n // 2)
            larger = self.findKth(A, 0, B, 0, n // 2 + 1)
            return (smaller + larger) / 2

    def findKth(self, A, index_a, B, index_b, k):
        if index_a == len(A):
            return B[index_b + k - 1]
        if index_b == len(B):
            return A[index_a + k - 1]

        if k == 1:
            return min(A[index_a], B[index_b])

        a = A[index_a + k // 2 - 1] if index_a + k // 2 <= len(A) else None
        b = B[index_b + k // 2 - 1] if index_b + k // 2 <= len(B) else None

        if b is None or (a is not None and a < b):
            return self.findKth(A, index_a + k // 2, B, index_b, k - k // 2)
        else:
            return self.findKth(A, index_a, B, index_b + k // 2, k - k // 2)
