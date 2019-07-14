class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        if L is None or len(L) == 0:
            return 0

        left, right = 1, max(L)

        while left + 1 < right:
            mid = left + (right - left) // 2

            if self.get_pieces(L, mid) >= k:
                left = mid
            else:
                right = mid

        if self.get_pieces(L, right) >= k:
            return right
        if self.get_pieces(L, left) >= k:
            return left
        return 0

    def get_pieces(self, L, length):
        count = 0

        for i in range(len(L)):
            count += L[i] // length

        return count
