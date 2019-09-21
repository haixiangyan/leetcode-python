import functools
class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        def compare(a, b):
            aFreq, aWord = a
            bFreq, bWord = b
            if aFreq != bFreq:
                return 1 if aFreq < bFreq else -1
            else:
                return 1 if aWord > bWord else -1
        if not words:
            return []

        store = {}
        # 存储 Frequency
        for word in words:
            if word not in store:
                store[word] = 1
            store[word] += 1

        # 排序
        heap = []
        for word in store:
            heap.append((store[word], word))
        heap = sorted(heap, key=functools.cmp_to_key(compare))

        # 生成结果
        results = []
        for i in range(len(heap)):
            if i >= k:
                break
            results.append(heap[i][1])

        return results
