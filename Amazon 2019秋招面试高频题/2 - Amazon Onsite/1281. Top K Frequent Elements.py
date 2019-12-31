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

        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        results = []
        for i in range(k):
            results.append(sorted_counts[i][0])

        return results