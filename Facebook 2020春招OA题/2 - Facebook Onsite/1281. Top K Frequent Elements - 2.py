import heapq


class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """

    def topKFrequent(self, nums, k):
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        heap = []
        for item in counts.items():
            heapq.heappush((-item[1], item[0]))

        results = []
        for i in range(k):
            count, value = heapq.heappop(heap)
            results.append(value)

        return results
