import heapq


class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """

    def topKFrequentWords(self, words, k):
        counts = {}
        heap = []

        # Count word frequency
        for word in words:
            if word not in counts:
                counts[word] = 0
            counts[word] += 1

        # Push to heap
        for word in counts:
            heapq.heappush(heap, (-counts[word], word))

        # Pop items from heap
        results = []
        for _ in range(k):
            _, word = heapq.heappop(heap)
            results.append(word)

        return results
