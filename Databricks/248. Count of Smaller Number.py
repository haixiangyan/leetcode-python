class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        A = sorted(A)
        n = len(A)
        results = []

        for query in queries:
            results.append(self.count(A, n, query))

        return results

    def count(self, A, n, query):
        if not A:
            return 0

        left, right = 0, n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] < query:
                left = mid
            else:
                right = mid

        if A[right] < query:
            return right + 1
        if A[left] < query:
            return left + 1
        return 0
