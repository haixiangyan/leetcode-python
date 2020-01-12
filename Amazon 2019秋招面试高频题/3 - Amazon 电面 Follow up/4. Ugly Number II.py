import heapq


class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """

    def nthUglyNumber(self, n):
        heap = [1]
        visited = {1}

        value = None

        for _ in range(n):
            value = heapq.heappop(heap)

            for factor in [2, 3, 5]:
                if value * factor not in visited:
                    visited.add(value * factor)
                    heapq.heappush(heap, value * factor)

        return value
